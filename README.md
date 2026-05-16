# 📚 AI Study Assistant — RAG-Based Learning System

An intelligent AI-powered Study Assistant built using **Retrieval-Augmented Generation (RAG)** that enables users to ask questions directly from PDF study materials and receive context-aware answers using Large Language Models.

The system processes PDF documents, converts them into embeddings, stores them in a vector database, retrieves relevant information, and generates accurate responses using a local LLM.

---

# 🚀 Features

* 📄 Multi-PDF document processing
* ✂️ Smart text chunking
* 🧠 Semantic embeddings generation
* 🔍 Vector similarity search using FAISS
* 🤖 AI-powered question answering
* 🌐 Interactive UI using Streamlit
* ⚡ Local LLM execution with Ollama + Llama3
* 📚 Retrieval-Augmented Generation (RAG) pipeline

---

# 🛠 Tech Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core Programming Language |
| LangChain             | LLM Orchestration         |
| FAISS                 | Vector Database           |
| Streamlit             | Web Application UI        |
| Ollama                | Local LLM Runtime         |
| Llama 3               | Large Language Model      |
| Sentence Transformers | Embedding Generation      |

---

# 🧠 System Architecture

```text
PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embeddings Generation
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Llama3 (LLM)
      │
      ▼
Final Answer
```

---

# 📂 Project Structure

```text
AI_STUDY_ASSIST/
│
├── app.py
├── requirements.txt
├── README.md
│
├── DATA/
│   ├── Gupta-Empire.pdf
│   ├── Harappan-Civilisation.pdf
│   └── Mauryan-Empire.pdf
│
├── MODULES/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── qa_chain.py
│
└── screenshots/
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd AI_STUDY_ASSIST
```

---

## 2️⃣ Create Virtual Environment

### Using Conda

```bash
conda create -n ritikenv python=3.11
conda activate ritikenv
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Dependencies

```txt
streamlit
langchain
langchain-community
faiss-cpu
sentence-transformers
pypdf
numpy
```

---

# 🤖 Install Ollama & Llama3

Install Ollama from the official website.

Then pull the Llama 3 model:

```bash
ollama run llama3
```

Start Ollama server:

```bash
ollama serve
```

---

# ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

# 💡 Example Questions

* Who founded the Gupta Empire?
* Explain Mauryan administration.
* What is the Harappan Civilization?
* Why is the Gupta period called the Golden Age of India?

---

# 🔥 Key Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embedding Models
* Similarity Search
* Local LLM Integration
* Prompt Engineering

---

# 📸 Screenshots

<img width="1366" height="768" alt="AI study assist" src="https://github.com/user-attachments/assets/42a04131-7094-43ee-8fce-81c08c83afea" />
<img width="1536" height="1024" alt="ChatGPT Image May 17, 2026, 12_55_34 AM" src="https://github.com/user-attachments/assets/c82d3d2c-8763-4f90-9c6e-3b76c1b69361" />



* Home Interface
* PDF Upload
* Question Answering
* Generated Responses

Example:

```text
screenshots/
├── home.png
├── upload.png
└── answer.png
```

---

# 🚀 Future Improvements

* Persistent FAISS index storage
* Chat history memory
* Multi-user authentication
* Cloud deployment
* Voice input support
* PDF highlighting and citations
* Support for DOCX and TXT documents

---

# 📈 Learning Outcomes

This project helped in understanding:

* Building end-to-end RAG systems
* Working with vector embeddings
* Implementing semantic retrieval
* Integrating local Large Language Models
* Developing AI-powered applications

---

# 👨‍💻 Author

## Ritik Shiwankar

AI & Machine Learning Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
