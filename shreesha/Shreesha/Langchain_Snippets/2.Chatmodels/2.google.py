from langchain_google_genai import ChatGoogleGenerativeAI  # Integration with Google's Gemini models
from dotenv import load_dotenv  # Loads API keys from .env file

load_dotenv()

# Create the chat model object
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro') 

# Create a variable to store the model's response
result = model.invoke("Explain the significance of the moon landing in one paragraph.")

print(result.content)
