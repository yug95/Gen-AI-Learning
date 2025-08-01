from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
#1.create a dynamic prompt template.
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)
#2.Create chat model
model = ChatHuggingFace(llm=llm)

#3.output parse to give us output in string format.
parser = StrOutputParser()  

#create chain.
chain = prompt | model | parser  

#invoke response for query.
result = chain.invoke({'topic':'cricket'}) 

print(result)

#to visulaize our chain.
#pip install grandalf
chain.get_graph().print_ascii() 