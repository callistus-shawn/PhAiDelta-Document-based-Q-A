from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

def get_chunk(text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separator=" ")
    texts = text_splitter.create_documents([text])
    docs = text_splitter.split_documents(texts)
    print(len(docs))
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embedding_function)
    return db