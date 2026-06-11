# 🤖 DocuChat AI

> Intelligent PDF Question Answering System powered by LangChain, ChromaDB, HuggingFace Embeddings, and Streamlit.

DocuChat AI is a Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them through a conversational interface. The system extracts text from PDFs, converts the content into vector embeddings, stores them in a Chroma vector database, and retrieves the most relevant information based on user queries.

---

## 🚀 Features

✅ Upload PDF documents

✅ Extract text from PDFs automatically

✅ Split large documents into semantic chunks

✅ Generate embeddings using HuggingFace models

✅ Store embeddings in ChromaDB

✅ Perform semantic similarity search

✅ Interactive chat-based interface

✅ Fast and efficient document retrieval

✅ Persistent vector database storage

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Web Interface |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Semantic Search |
| PyPDFLoader | PDF Processing |

---

## 📂 Project Structure

```text
DocuChat-AI/
│
├── app.py
├── chroma_db/
├── requirements.txt
├── README.md
│
└── assets/
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RushikeshPimpale/DocuChat-AI.git

cd DocuChat-AI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 📖 Workflow

### Step 1: Upload PDF

Users upload a PDF document through the Streamlit interface.

### Step 2: Text Extraction

The application extracts text using:

```python
PyPDFLoader
```

### Step 3: Text Chunking

The document is split into manageable chunks using:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size = 1000
chunk_overlap = 200
```

### Step 4: Embedding Generation

Each chunk is converted into vector embeddings using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

### Step 5: Store in ChromaDB

Generated embeddings are stored inside:

```text
chroma_db/
```

### Step 6: User Query

The user asks a question related to the uploaded document.

### Step 7: Similarity Search

ChromaDB retrieves the top relevant chunks.

### Step 8: Generate Response

Relevant content is displayed to the user through the chat interface.

---

## 🧠 Embedding Model

The project uses:

```python
sentence-transformers/all-MiniLM-L6-v2
```

Benefits:

- Lightweight
- Fast inference
- High-quality semantic embeddings
- Open-source

---

## 📦 Dependencies

```txt
streamlit
langchain
langchain-community
langchain-chroma
langchain-huggingface
chromadb
sentence-transformers
pypdf
```

Install manually:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install langchain-chroma
pip install langchain-huggingface
pip install chromadb
pip install sentence-transformers
pip install pypdf
```

---

## 💡 Example Usage

### Upload

```text
Research_Paper.pdf
```

### Ask Questions

```text
What is the main objective of this paper?

Summarize chapter 3.

What are the key findings?

Explain the methodology section.
```

### Output

```text
Relevant information extracted from the uploaded PDF.
```

---

## 🎯 Use Cases

### Education

- Study Assistant
- Research Paper Analysis
- Academic Notes Search

### Business

- Company Reports
- Financial Statements
- Policy Documents

### Legal

- Contract Review
- Legal Documentation Search

### Healthcare

- Medical Research Papers
- Clinical Documentation

### Personal Productivity

- Ebook Search
- Resume Analysis
- Documentation Assistant

---

## 🔮 Future Enhancements

### AI Integration

- OpenAI GPT-4 Integration
- Gemini Integration
- Claude Integration

### RAG Improvements

- Multi-PDF Support
- Metadata Filtering
- Advanced Retrieval

### User Experience

- Chat Memory
- Conversation History
- Dark Mode

### Document Intelligence

- PDF Summarization
- OCR Support
- Keyword Extraction
- Citation Generation

### Deployment

- Docker Support
- AWS Deployment
- Azure Deployment
- Render Deployment

---

## 📊 Skills Demonstrated

This project demonstrates practical experience in:

- Retrieval-Augmented Generation (RAG)
- Natural Language Processing (NLP)
- Vector Databases
- Semantic Search
- LangChain Framework
- Streamlit Development
- Embedding Models
- Document Intelligence Systems

---

## 🌟 Why This Project?

Traditional keyword search often fails to understand the meaning behind user queries.

DocuChat AI solves this problem using semantic search and vector embeddings, enabling users to interact naturally with PDF documents and retrieve contextually relevant information.

This project showcases modern AI engineering concepts widely used in enterprise knowledge management systems and Generative AI applications.

---

## 🤝 Contributing

Contributions are welcome.

### Steps

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create Pull Request

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project.

---

## 👨‍💻 Author

### Rushikesh Pimpale

AI/ML Engineer | Generative AI Enthusiast

GitHub:

https://github.com/RushikeshPimpale

LinkedIn:

https://linkedin.com/in/rushikesh-pimpale

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share with others

---

### Made with ❤️ using Python, LangChain, ChromaDB, HuggingFace, and Streamlit.
