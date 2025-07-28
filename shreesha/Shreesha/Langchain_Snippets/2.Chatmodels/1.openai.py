from langchain_openai import ChatOpenAI  # Integration between LangChain and OpenAI
from dotenv import load_dotenv  # Loads API keys from .env file

load_dotenv()

# Create the chat model object
model = ChatOpenAI(model='gpt-4', temperature=0) 
# Define the chat model you want to use
# Temperature controls creativity: 0 = deterministic, ≥1 = more creative
# max_completion_tokens limits the length of the model's output


result = model.invoke("List three key benefits of using LangChain for AI apps.")  # invoke() is used to communicate with LLMs
# Create a variable to store the model's response

print(result.content)

# Using .content gives only the model's text output
# Without .content, it prints the full message object (e.g., AIMessage(...))
