
import os
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate ,load_prompt



os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")



templete = load_prompt("prompt.json")


chain = templete | model
response = chain.invoke({"state": "jharkhand india"})
print(response.content)
