from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a summary on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 3 quiz questions from the following text \n {text}',
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)

# Create chat model
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Phototsynthesis'})

print(result)

#chain.get_graph().print_ascii()

"""
prompt1 :takes the initial input and turns it into a structured prompt.
model uses that prompt to generate a response.
parser: cleans or extracts useful information from the model's output.
prompt2: takes that parsed info and creates a second prompt.
model then generates a second response using that new prompt.
parser: processes the final output to extract the final result.
"""
