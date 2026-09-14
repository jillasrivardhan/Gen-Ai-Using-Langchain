from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",)

texts = ["This is a test document.", "This is another test document."]

embeddings = embedding_model.embed_documents(texts)
# embeddings = embedding_model.embed_query(texts)

print(str(embeddings))