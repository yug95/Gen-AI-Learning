from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. Create a chat prompt template
chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name='chat_history'),  # This will insert the past conversation here
    ('human', '{query}')  # This is where the user's current question goes
])

# 2. Initialize a list to store chat history
chat_history = []

# 3. Load chat history from a file
with open('chat_history.txt') as f:
    # f.readlines() reads each line from the file as a list of strings
    # chat_history.extend(...) adds each of those lines to the chat_history list
    chat_history.extend(f.readlines())

# 4. Print the loaded chat history
print("Chat History (raw text):")
print(chat_history)

# 5. Create the final prompt by combining the chat history and the user's new query
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'Where is my refund'
})

# 6. Print the generated prompt
print(prompt)
