#Closed source embedding model
#This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional 
#dense vector space and can be used for tasks like clustering or semantic search.

from langchain_huggingface import HuggingFaceEmbeddings

# Load the embedding model from Hugging Face
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# For a single text input, use:
# text = "Python is the best programming language."
# vector = embedding.embed_query(text)

# For multiple text inputs, use a list:
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for each document
vector = embedding.embed_documents(documents)

print(str(vector))