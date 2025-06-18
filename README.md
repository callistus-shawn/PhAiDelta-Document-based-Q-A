# Document based Q&A System
* This project is a Retrieval-Augmented Generation (RAG) web application built using FastAPI. It allows users to upload documents (such as PDFs or text files), which are then chunked, embedded using Sentence Transformers, and stored in a vector database for efficient semantic search. 
* When a user submits a question, using Langhchain, the system retrieves the most relevant text chunks from the uploaded documents using similarity search and sends them to a Large Language Model (LLM) (e.g., OpenAI or Gemini) to generate context-aware answers.


# Image Style Transfer using CycleGANs
Image style transfer involves modifying an image to adopt the visual style of another image while preserving its original content. CycleGAN (Cycle-Consistent Generative Adversarial Network) enables this transformation without requiring paired training examples. 
* It uses two GANs, each consisting of a generator and a discriminator, to translate images between two domains. 
* The key innovation is cycle consistency, where an image translated to the other domain and then back should closely resemble the original, ensuring content preservation. The model is trained using both cycle consistency loss and adversarial loss, achieving high-quality style transfer.
  
### 🗂️ Project Files Description

### 📁 `fileapi/` – Main FastAPI Application

| File         | Description |
|--------------|-------------|
| `app.py`     | Initializes the FastAPI app, mounts static files, and includes API routers. Sets up the main application context. |
| `main.py`    | Entry point for starting the FastAPI server. Imports the `app` instance from `app.py` and runs with Uvicorn. |
| `route.py`   | Central routing module where all API endpoints are declared (e.g., file upload, query handling). Uses FastAPI's `APIRouter`. |
| `model.py`   | Defines Pydantic data models used for request/response validation (e.g., handling input questions and file metadata). |


---

### 📁 `fileapi/helper/` – Utility Modules

| File       | Description |
|------------|-------------|
| `chunk.py` | Breaks large documents into smaller overlapping text chunks, which are critical for effective embedding and retrieval. |
| `db.py`    | Handles operations on the vector store: saving/loading embeddings, and performing similarity search based on embeddings. |

---

### 📁 `fileapi/rag/` – RAG Logic (Retrieval-Augmented Generation)

| File           | Description |
|----------------|-------------|
| `function.py`  | **Core RAG engine**: Handles embedding of text using Sentence Transformers, stores embeddings into the vector DB, retrieves top-k relevant chunks for a query, and communicates with the LLM for generating final answers. Integrates logic from both `upload.py` and `question.py`. |

---
