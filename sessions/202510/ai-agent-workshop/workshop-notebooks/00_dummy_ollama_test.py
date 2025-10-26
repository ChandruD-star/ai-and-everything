from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="smollm:latest",
    temperature=0,
    base_url='http://localhost:11434',
    num_predict=20
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)