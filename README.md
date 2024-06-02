<a href="https://github.com/anmolwadhwaxx/RAG" target="_blank">
    <img src="https://via.placeholder.com/1000x300.png?text=LLM+Chat+App" target="_blank" alt="LLM Chat App" width="1000">
</a>

# LLM Chat App

[![RepoRater](https://repo-rater.eddiehub.io/api/badge?owner=yourusername&name=llm-chat-app)](https://repo-rater.eddiehub.io/rate?owner=yourusername&name=llm-chat-app&format=percentage)

## Description

LLM Chat App is a web application built with Streamlit, LangChain, and OpenAI to allow users to upload PDF files and interact with their content using natural language queries.

### Features

- Upload a PDF file and extract its text content.
- Split the text into manageable chunks.
- Use OpenAI's language model to answer questions about the PDF content.
- Save and load text chunks for efficient processing.
- Submit queries and chatbot responses to a Google Form for logging.

## Live Demo

You can access the live demo of the app at the following links:
- [Streamlit Deployment - https://anmolpdf.streamlit.app](https://anmolpdf.streamlit.app)
- [Render Deployment - https://rag-i7rz.onrender.com](https://rag-i7rz.onrender.com)

## Setup

There are some necessary steps to get the project up and running.

### Prerequisites

- Python 3.8 or higher
- Create an OpenAI account and get your API key from [OpenAI](https://platform.openai.com/).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/llm-chat-app.git
    cd llm-chat-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file in the project root.
    - Add your OpenAI API key and any other necessary configurations to the `.env` file.
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the App

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to the provided local URL (usually `http://localhost:8501`).

3. Use the sidebar to upload a PDF file and interact with the chatbot.

## File Structure

- `app.py`: Main application file containing the Streamlit app.
- `requirements.txt`: List of Python dependencies.
- `.env.example`: Example environment file for storing API keys and configuration.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## About

This app is an LLM-powered chatbot built using:
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI](https://platform.openai.com/docs/models) LLM model

Made with ❤️ by [Anmol Wadhwa](https://linkedin.com/in/anmol-wadhwa) in India

## Acknowledgements

- Special thanks to the contributors of Streamlit, LangChain, and OpenAI for their fantastic libraries and APIs.
