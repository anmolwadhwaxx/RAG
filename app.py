import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks import get_openai_callback
import os
import requests

# Sidebar contents
with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Anmol Wadhwa](https://linkedin.com/in/anmol-wadhwa)')

load_dotenv()

def submit_query_to_google_form(query, response):
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScnwq4U7iLOcq1VKggFp-RdBFF64cd5b3evesGNPcCDbFM9Zw/formResponse'
    form_data = {
        'entry.112538290': query,
        'entry.659081082': response  # Replace with actual entry ID for the chatbot response
    }
    response = requests.post(form_url, data=form_data)
    return response

def main():
    st.header("Chat with PDF")

    # Initialize VectorStore to None
    VectorStore = None

    # Upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    # Process the PDF file
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # Adjust chunk size as needed
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        # Load or create VectorStore
        store_name = pdf.name[:-4]
        st.write(f'{store_name}')

        try:
            if os.path.exists(f"{store_name}.pkl"):
                with open(f"{store_name}.pkl", "rb") as f:
                    text_chunks = pickle.load(f)  # Load only the text chunks
                    embeddings = OpenAIEmbeddings()
                    VectorStore = FAISS.from_texts(text_chunks, embedding=embeddings)
                    st.write('Embeddings Loaded (recreated) from the Disk')
            else:
                embeddings = OpenAIEmbeddings()

                # Filter out empty chunks before creating VectorStore
                non_empty_chunks = [chunk for chunk in chunks if chunk.strip()]

                # Check if there are any non-empty chunks remaining
                if non_empty_chunks:
                    VectorStore = FAISS.from_texts(non_empty_chunks, embedding=embeddings)
                    with open(f"{store_name}.pkl", "wb") as f:
                        pickle.dump(non_empty_chunks, f)  # Pickle only the text chunks
                        st.write('Embeddings Saved to Disk')
                else:
                    st.error("Not enough text found in the PDF for processing.")

        except FileNotFoundError:
            st.error("Pickled file not found.")
        except Exception as e:
            st.error(f"Error loading or creating VectorStore: {e}")

        if VectorStore is not None:
            # Accept user questions/query
            query = st.text_input("Ask questions about your PDF file:")

            if query:
             
        

                docs = VectorStore.similarity_search(query=query, k=3)

                llm = OpenAI()
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)
                    st.write(response)

                # Submit query and chatbot response to Google Form
                form_response = submit_query_to_google_form(query, response)
            

if __name__ == '__main__':
    main()
