
from google.colab import userdata
from langchain_google_genai import GoogleGenerativeAI
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

model = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(template="Generate {mood_type}insight on {topic} in 50 words ", input_variables = ["mood_type", "topic"])

runner = RunnableParallel(
          happy = prompt.partial(mood_type= "happy ") |model|parser  ,
          sad = prompt.partial(mood_type= "sad")|model|parser
  )


result = runner.invoke({"topic":"electric car"})

for mood, response in result.items():
  print(f"{mood}: \n{response}")
    
    



