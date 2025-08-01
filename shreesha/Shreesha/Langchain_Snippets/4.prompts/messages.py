#instead of using dictornary to add labels to chat history we use this built-in class messages

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)

# Create chat model
model = ChatHuggingFace(llm=llm)

#create a list of messages.
messages=[    
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages) #send the prompt(list of messages) to receive response from ai

#the response received from ai now gets appended to the list of messages we created for complete context
messages.append(AIMessage(content=result.content))

print(messages)
