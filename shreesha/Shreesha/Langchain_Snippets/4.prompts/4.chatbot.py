#without chat history

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Set up HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  # your model
    task="text-generation"
)

# Create chat model
model = ChatHuggingFace(llm=llm)

chat_history = []  #define a list to store chat history.

# Interactive loop
while True:
    user_input = input("You: ")
    chat_history.append(user_input) #each time a user types a message add it to chat history
    if user_input == "exit":
        break
    result = model.invoke(chat_history)  #well send our chat history to the model everytime
    chat_history.append(result.content) #the result we get from the model also should be store in chat_history.
    print("AI:", result.content)
print(chat_history)
    

