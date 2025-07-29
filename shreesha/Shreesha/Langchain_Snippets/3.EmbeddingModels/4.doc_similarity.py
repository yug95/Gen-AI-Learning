from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
#`cosine_similarity` from `sklearn.metrics.pairwise` calculates how similar two vectors are based on the cosine 
# of the angle between them, with values ranging from -1 (opposite) to 1 (identical).
import numpy as np

load_dotenv()

# Create OpenAI embedding object (300-dimensional vectors)
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# Sample documents about major tech companies
documents = [
    "Apple Inc. is known for its innovative products like the iPhone, MacBook, and Apple Watch.",
    "Google specializes in internet-related services, including search, advertising, and cloud computing.",
    "Microsoft develops software products like Windows OS and productivity tools such as Microsoft Office.",
    "Amazon is a global e-commerce leader and also dominates the cloud market with AWS.",
    "Tesla is a leader in electric vehicles and renewable energy solutions, founded by Elon Musk."
]

# User query
query = "What does Tesla do and what is it famous for?"

# Generate embeddings for documents and query
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compute cosine similarity scores between query and each document
# Input must be 2D, so we wrap query_embedding in a list
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Sort by similarity score in descending order and get the best match
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Print the most relevant document
print(query)
print(documents[index])
print("Similarity score is:", score)