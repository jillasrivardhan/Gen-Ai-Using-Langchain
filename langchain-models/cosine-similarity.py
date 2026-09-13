from sklearn.metrics.pairwise import cosine_similarity

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
   model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
  "virat kohli is a great cricketer.",
  "sachin tendulkar is a great cricketer.",
  "messi is a great footballer.",
  "ronaldo is a great footballer.",
  "elon musk is a great entrepreneur."]

embeddings = embedding_model.embed_documents(texts)

query = "Tell me about virat kohli."
query_embedding = embedding_model.embed_query(query)

similarity_scores = cosine_similarity([query_embedding], embeddings)


for i,texts in enumerate(texts):
   print(f"Text: {texts[i]} - Similarity Score: {similarity_scores[0][i]}")