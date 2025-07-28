from langchain_openai import OpenAI  # Integration package between LangChain and OpenAI
from dotenv import load_dotenv       # Loads API keys from .env file

load_dotenv()

# Create the LLM object
llm = OpenAI(model='gpt-3.5-turbo-instruct')  # Define the LLM model you want to use

# Create a variable to store the LLM response
result = llm.invoke("What is AI.")  # invoke() is used to communicate with LLMs

print(result)
