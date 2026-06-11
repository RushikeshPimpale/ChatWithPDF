import os
import tempfile
import streamlit as st

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI PDF Chatbot")

# ---------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------
@st.cache_resource
def load_vectorstore():

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    return db

db = load_vectorstore()

# ---------------------------------
# TEXT SPLITTER
# ---------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# ---------------------------------
# SESSION STATE
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# SIDEBAR
# ---------------------------------
with st.sidebar:

    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type="pdf"
    )

    if uploaded_file is not None:

        if st.button("Process PDF"):

            with st.spinner("Processing PDF..."):

                # Save temp PDF
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    temp_pdf_path = tmp_file.name

                # Load PDF
                loader = PyPDFLoader(temp_pdf_path)
                documents = loader.load()

                # Split text
                docs = text_splitter.split_documents(documents)

                # Add to ChromaDB
                db.add_documents(docs)

                st.success("PDF Added Successfully ✅")

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------
# DISPLAY CHAT
# ---------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------
# USER INPUT
# ---------------------------------
user_input = st.chat_input("Ask something about your PDF...")

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            # Similarity Search
            results = db.similarity_search(user_input, k=3)

            response = ""

            for doc in results:
                response += doc.page_content + "\n\n"

            if response.strip() == "":
                response = "No relevant information found."

            st.markdown(response)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )