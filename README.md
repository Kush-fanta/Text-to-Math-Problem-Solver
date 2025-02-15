---

# Math Problem Solver and Data Search Assistant

This project is a Streamlit-based web application that uses Groq's API and LangChain to solve mathematical problems and search for information using Wikipedia. The application is designed to provide step-by-step solutions to math problems and assist with data searches.

## Features

- **Math Problem Solver**: Solves mathematical problems using logical reasoning and step-by-step solutions.
- **Wikipedia Search**: Searches Wikipedia for information related to the user's query.
- **Interactive Chat Interface**: Provides an interactive chat interface for user queries and responses.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- Groq API Key

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/text-to-math-problem-solver.git
   cd text-to-math-problem-solver
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Running the Application Locally

1. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Run the Streamlit App**:
   ```bash
   streamlit run math_app.py
   ```

3. **Access the Application**:
   Open your web browser and go to `http://localhost:8501` to interact with the Math Problem Solver and Data Search Assistant.

## Usage

1. **Enter Groq API Key**:
   - On the sidebar, enter your Groq API key.

2. **Ask a Question**:
   - Enter your mathematical question or search query in the text area.
   - Click the "Find the Answer" button to get the solution or information.

3. **View Results**:
   - The application will display the solution or search results in the chat interface.

## Deployment

### Deploying on Streamlit Cloud

1. **Update `requirements.txt`**:
   - Ensure all dependencies in `requirements.txt` are valid and correctly spelled. For example:
     ```plaintext
     langchain
     python-dotenv
     ipykernel
     langchain_community
     pypdf
     bs4
     arxiv
     pymupdf
     wikipedia
     langchain-text-splitters
     langchain-openai
     sentence_transformers
     langchain_huggingface
     faiss-cpu
     chromadb
     langchain-chroma
     langchain_groq
     uvicorn
     fastapi
     langserve
     numexpr
     ```

2. **Push Changes to GitHub**:
   - Commit and push your changes to the repository:
     ```bash
     git add requirements.txt
     git commit -m "Fix dependency issues"
     git push origin main
     ```

3. **Deploy on Streamlit**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy your app by connecting your GitHub repository.

4. **Monitor Logs**:
   - If the deployment fails, check the logs in the Streamlit Cloud dashboard for detailed error messages.

## Dependencies

The project relies on the following Python packages:

- `streamlit`
- `langchain`
- `langchain_groq`
- `langchain_community`
- `wikipedia`
- `python-dotenv`
- `pypdf`
- `bs4`
- `arxiv`
- `pymupdf`
- `sentence_transformers`
- `faiss-cpu`
- `chromadb`
- `uvicorn`
- `fastapi`
- `langserve`
- `numexpr`

For a complete list of dependencies, refer to the `requirements.txt` file.

## Acknowledgments

- Groq for providing the API.
- LangChain for the framework.
- Streamlit for the web interface.

---
