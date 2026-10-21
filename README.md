# Agentic RAG with EmbeddingGemma

A locally running Agentic Retrieval-Augmented Generation (RAG) application that uses Google's EmbeddingGemma for document embeddings and Llama 3.2 for generating answers. The project combines semantic search, a vector database, and an AI agent to answer questions using retrieved information.

## Overview

Retrieval-Augmented Generation (RAG) improves question answering by retrieving relevant information from a knowledge base before generating a response.

This project uses local models through Ollama, Agno for agent orchestration, LanceDB for vector storage, and Streamlit for the user interface.

## Features

- **Local AI Models:** Uses Ollama to run EmbeddingGemma and Llama 3.2 locally.
- **Semantic Search:** Uses vector embeddings to retrieve relevant information.
- **Agentic RAG:** Uses an Agno agent configured to search the knowledge base before answering.
- **Vector Database:** Uses LanceDB for local vector storage and similarity search.
- **Interactive Interface:** Uses Streamlit to provide a browser-based interface.
- **Privacy-Focused Design:** Supports local model inference and local vector storage.

## Technologies Used

- Python
- Streamlit
- Agno
- Ollama
- Google EmbeddingGemma
- Llama 3.2
- LanceDB
- PyPDF

## Architecture

1. **Document Source:** Documents provide information for the knowledge base.
2. **Embedding Generation:** EmbeddingGemma converts text into vector embeddings.
3. **Vector Storage:** LanceDB stores embeddings for retrieval.
4. **Information Retrieval:** The knowledge base searches for relevant information.
5. **Answer Generation:** Llama 3.2 generates responses using the retrieved context.
6. **User Interface:** Streamlit provides the interface for interacting with the application.

## Project Structure

```text
agentic_rag_embedding_gemma/
├── agentic_rag_embeddinggemma.py
├── requirements.txt
├── ollama.png
├── README.md
└── .gitignore
```

The `tmp/lancedb/` directory is used for local vector database storage and is excluded from GitHub.

## Prerequisites

Before running the project, install:

- Python
- Git
- Ollama

Your system also needs sufficient memory and storage to run the local language models.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mohana-Rupa/agentic-rag-embeddinggemma.git
cd agentic-rag-embeddinggemma
```

### 2. Create a virtual environment

On Windows, run:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Download the required Ollama models

```powershell
ollama pull embeddinggemma:latest
ollama pull llama3.2:latest
```

If these models are already installed, downloading them again is unnecessary.

To check your installed models, run:

```powershell
ollama list
```

### 5. Run the application

From the project directory, run:

```powershell
streamlit run agentic_rag_embeddinggemma.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to access the application.

## Configuration

The application uses the following configuration:

| Component | Configuration |
|---|---|
| Embedding model | `embeddinggemma:latest` |
| Embedding dimensions | 768 |
| Language model | `llama3.2:latest` |
| Agent framework | Agno |
| Vector database | LanceDB |
| Vector table | `documents` |
| Database location | `tmp/lancedb` |
| User interface | Streamlit |

## Privacy and Data Handling

The project is designed to run language models locally through Ollama and store vector data locally using LanceDB.

Internet access may still be required to install Python dependencies, download models, or retrieve documents from external sources if that functionality is configured.

## Limitations

- Answer quality depends on the relevance and quality of the indexed documents.
- Local model performance depends on available hardware resources.
- Useful retrieval-based answers require documents to be available in the knowledge base.
- Model files and the local vector database are not included in this GitHub repository.
- The available application code determines which document formats and ingestion workflows are supported.

## Future Enhancements

- Improve document ingestion and indexing workflows.
- Support additional document formats.
- Improve retrieval quality and response relevance.
- Add source references to generated answers.
- Improve error handling and application performance.
- Add evaluation tools for retrieval and answer quality.

## Author

**Mohana Rupa**

GitHub: [Mohana-Rupa](https://github.com/Mohana-Rupa)

## License

No license has been specified yet. Add an appropriate open-source license if you intend to allow others to reuse or modify this project.

---

*This project is intended for educational and research purposes.*
