from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from google.colab import userdata
from langchain_google_genai import GoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

model = GoogleGenerativeAI(model="gemini-1.5-flash")
def add_label(airesponse) :
  return f"Label: {airesponse}"

label = RunnableLambda(add_label)


prompt1 = PromptTemplate(template="gnerate intersiting fact about {topic}")
chain1 =  prompt1 | model | parser

prompt2 = PromptTemplate(template="create a interseting tweet using this {facts} with relevent hastages")
chain2 = prompt2 | model

sequencial_chain = {"facts" :chain1} | chain2 | add_label

try:
  response = sequencial_chain.invoke({"topic" : "pasta"})
  print(response)

except Exception as e:
  print(f"error : {e}")
