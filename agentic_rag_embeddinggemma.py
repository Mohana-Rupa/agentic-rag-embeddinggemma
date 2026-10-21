import streamlit as st
from agno.agent import Agent
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.ollama import Ollama
from agno.vectordb.lancedb import LanceDb, SearchType



st.set_page_config(
    page_title="Agentic RAG with EmbeddingGemma",
    page_icon="🔥",
    layout="wide"
)

# KNOWLEDGE BASE


@st.cache_resource
def load_knowledge_base():
    return Knowledge(
        vector_db=LanceDb(
            table_name="documents",
            uri="tmp/lancedb",
            search_type=SearchType.vector,
            embedder=OllamaEmbedder(
                id="embeddinggemma:latest",
                dimensions=768
            ),
        ),
    )

kb = load_knowledge_base()


# AGENT


agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    knowledge=kb,
    instructions=[
        "Search the knowledge base before answering.",
        "Base answers only on retrieved information.",
        "Use headings and bullet points when useful.",
        "Provide clear and concise responses."
    ],
    search_knowledge=True,
    markdown=True,
)


# SIDEBAR


with st.sidebar:

    st.image("ollama.png", width=120)

    st.header("🌐 Add PDF URL")

    pdf_url = st.text_input(
        "PDF URL",
        placeholder="https://arxiv.org/pdf/1706.03762.pdf"
    )

    if st.button("➕ Add URL"):

        if not pdf_url:
            st.error("Please enter a PDF URL")

        else:

            try:
                with st.spinner("Loading PDF and creating embeddings..."):

                    print(f"Loading: {pdf_url}")

                    kb.add_content(url=pdf_url)

                    print("Finished loading")

                st.success("PDF added successfully!")

            except Exception as e:
                st.error(f"Error loading PDF: {e}")


# MAIN UI


st.title("🔥 Agentic RAG with EmbeddingGemma")

st.markdown(
    """
This application runs completely locally using:

- EmbeddingGemma for embeddings
- LanceDB for vector storage
- Llama 3.2 for answer generation
- Ollama for local model serving

Add a PDF URL and ask questions about it.
"""
)

query = st.text_input(
    "Ask a question about your document:"
)

if st.button("🚀 Get Answer"):

    if not query:
        st.warning("Please enter a question.")

    else:

        try:

            response_box = st.empty()
            response_text = ""

            with st.spinner("Generating answer..."):

                result = agent.run(
                    query,
                    stream=True
                )

                for chunk in result:

                    if chunk.content:
                        response_text += chunk.content
                        response_box.markdown(response_text)

        except Exception as e:
            st.error(f"Error: {e}")


# INFO


with st.expander("📖 How It Works"):

    st.markdown(
        """
### Workflow

1. PDF URL is loaded
2. Text is extracted
3. EmbeddingGemma creates embeddings
4. LanceDB stores vectors
5. User asks a question
6. Relevant chunks are retrieved
7. Llama 3.2 generates an answer

### Models

- Embedding Model: embeddinggemma:latest
- LLM: llama3.2:latest
- Vector Database: LanceDB
- Framework: Agno
"""
    )

# https://arxiv.org/pdf/2606.23585
  