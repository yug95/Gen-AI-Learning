from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from langchain_google_genai import GoogleGenerativeAI
from google.colab import userdata
import os

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

model = GoogleGenerativeAI(model="gemini-1.5-flash")
parser = StrOutputParser()
prompt = PromptTemplate(template="tell me crazy insight about {topic} in 2 lines", input_variables=["topic"])
chain = prompt| model|parser
chain2 = prompt|model
try:
  response = chain2.invoke({"topic" :"lion"})
  print(response)
except exception as e:
  print(f"error: {e}")