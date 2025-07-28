from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct", #the model we are using
   task="text-generation" #what task we'll be performing with this model
)

model = ChatHuggingFace(llm=llm)


result = model.invoke("Write a short poem about the sunrise.")

print(result.content)
