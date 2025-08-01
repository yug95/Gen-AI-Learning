from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_core.output_parsers import StrOutputParser
from google.colab import userdata
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool

parser = StrOutputParser()
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")


@tool
def add_special_number(num: int) -> int:
    """ Add Special number """
    return num + 10

def check_tool_call(response : object ):
  if  not response.tool_calls:
    return response
  else:
    print("calling tool.....")
    for tool_call in response.tool_calls:
        # print(f"Tool to call: {tool_call['name']}")
        # print(f"Arguments: {tool_call['args']}")

        if tool_call['name'] == 'add_special_number':
          return add_special_number.invoke(tool_call['args'])

runnable = RunnableLambda(check_tool_call)


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
model_with_tools = model.bind_tools([add_special_number])

chain = model_with_tools | runnable
chain.invoke("add special number to 5")

