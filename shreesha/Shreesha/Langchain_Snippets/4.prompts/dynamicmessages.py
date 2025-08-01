#ChatPrompt-template.
from langchain_core.prompts import ChatPromptTemplate

# Create the chat prompt template w placeholders.
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# Fill in the template with user-provided values
prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

# Show the final prompt messages
print(prompt)