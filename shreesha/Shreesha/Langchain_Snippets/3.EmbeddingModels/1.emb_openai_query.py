#ONLY FOR GENERATING SINGLE QUERY EMBEDDING.

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Create an OpenAI embedding object with a specific model and dimension
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# We're generating 32-dimensional vectors
# Smaller vectors (like 32) capture less context but are cheaper
# Larger vectors capture more context but cost more

# Generate the embedding for the given text
result = embedding.embed_query("python is the best programming language")

# Print the resulting 32-dimensional vector
print(str(result))


# Use `str(result)` only if you want to **print or save** the embedding as text.
# If you need to **compare embeddings** or **store them in a vector database**, use the original **list format**, not the string.

