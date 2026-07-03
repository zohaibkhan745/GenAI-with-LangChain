from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text_generation"
)
chat_model = ChatHuggingFace(llm=llm)
chat = chat_model.invoke("who was the first president of the US?")
print(chat.content)