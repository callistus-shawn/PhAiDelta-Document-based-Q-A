## 🗂️ Project Files Description

### 📁 `fileapi/` – Main FastAPI Application

| File | Description |
|------|-------------|
| `app.py` | Initializes the FastAPI app, mounts static files, and includes API routers. Sets up the main application context. |
| `main.py` | Entry point when starting the FastAPI server. Imports `app` from `app.py` and runs with Uvicorn. |
| `route.py` | Central routing module where endpoints are declared (e.g., for upload, ask). Uses FastAPI's `APIRouter`. |
| `model.py` | Defines Pydantic data models for request and response validation (e.g., for handling input questions). |
| `upload.py` | Handles file upload logic, including saving files, validating formats, and triggering embedding processes. |
| `question.py` | Accepts a user query, retrieves relevant chunks from FAISS, and sends them to the LLM for response generation. |

---

### 📁 `fileapi/helper/` – Utility Modules

| File | Description |
|------|-------------|
| `__init__.py` | Makes this directory a Python package. |
| `chunk.py` | Logic for breaking large documents into smaller overlapping text chunks (important for embedding and retrieval). |
| `db.py` | Manages vector store using FAISS: saving/loading embeddings, performing similarity search. |

---

### 📁 `fileapi/rag/` – RAG Logic (Retrieval-Augmented Generation)

| File | Description |
|------|-------------|
| `__init__.py` | Marks this directory as a module. |
| `function.py` | **Core module**: handles embedding of text using a sentence-transformer model, stores embeddings in FAISS, and retrieves the top-k relevant chunks for a given query. This is the RAG engine. |

---

### 📁 `tests/` – Test Suite Placeholder

| File | Description |
|------|-------------|
| `__init__.py` | Makes this directory a Python package. You can add test files here to verify the components (e.g., test uploading, embedding, retrieval). |

---

### 🧠 Workflow Summary (File Relationships)

```text
User Uploads File
     ↓
upload.py → chunk.py → function.py → db.py
     ↓
Embeddings stored in FAISS

User Asks Question
     ↓
question.py → function.py → db.py → LLM (e.g., OpenAI)
     ↓
Returns Answer
