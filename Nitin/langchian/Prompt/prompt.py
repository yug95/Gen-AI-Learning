import os
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")


templete = PromptTemplate(template="tell me the capital of {state}", input_variables=["state"],)

# print(templete)
# chain = templete | model
# chain.invoke({"state": "jharkhand india"})

final_prompt = templete.invoke({ "assam india"})
print(final_prompt)

aimsg = model.invoke(final_prompt)
print(aimsg.content)
