from dotenv import load_dotenv
load_dotenv()
# google does not expose basellm model so i import chat model
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response = llm.invoke("who is Micheal Jackson?")
print(response.content)