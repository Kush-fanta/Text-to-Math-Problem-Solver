import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# Set up Streamlit app
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant")
st.title("Text to Math Problem Solver using Google Gemma 2")

# Groq API Key Input
groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")
if not groq_api_key:
    st.info("Please enter your Groq API Key to continue")
    st.stop()

# Initialize Groq LLM
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize Tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching Wikipedia to find information."
)

# Initialize Math Tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for solving mathematical problems."
)

# Math Problem Tool
prompt = """
You are an agent tasked with solving the user's mathematical question. Logically arrive at the solution and display it step-by-step for the question below.
Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning",
    func=chain.run,
    description="A tool for solving math problems using logical reasoning."
)

# Initialize Agent
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Initialize Session State for Messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math ChatBot who can solve any math problem!"}
    ]

# Display Previous Messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Function to Generate Response
def generate_response(user_ques):
    try:
        response = assistant_agent.invoke({'input': user_ques})
        return response['output']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# User Interaction
question = st.text_area("Enter the Question")
if st.button("Find the Answer"):
    if question:
        with st.spinner("Generating response..."):
            # Add user question to session state
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            # Generate and display response
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(question, callbacks=[st_cb])

            # Add assistant response to session state
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
    else:
        st.warning("Please enter a question.")