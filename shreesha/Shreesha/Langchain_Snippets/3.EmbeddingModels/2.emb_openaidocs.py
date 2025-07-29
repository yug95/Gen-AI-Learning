#FOR GENERATING MULTIPLE QUERY EMBEDDINGS.

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI embedding object with a specific model and dimension
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# List of multiple text inputs to generate embeddings for
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for each document in the list
# Note: We use embed_documents (not embed_query) for multiple inputs
result = embedding.embed_documents(documents)

# Print the list of embeddings (one per document)
print(str(result))
