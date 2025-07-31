#W/O USING CHAINS:
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Set up HuggingFace endpoint
llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)

# Create chat model
model = ChatHuggingFace(llm=llm)

# Ask user for name
name = input("Enter your name: ")

# Define the prompt template
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# Fill the template with user input
prompt = template2.invoke({'name': name})

#to use chains replace the above prompt line w chain line. 
# chain = template | model   #what is does chain: prompt → model


# Get the result from the model
result = model.invoke(prompt)

# Print the output
print(result.content)

