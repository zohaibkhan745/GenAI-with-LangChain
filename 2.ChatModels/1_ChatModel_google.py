from dotenv import load_dotenv
load_dotenv()
# google does not expose basellm model so i import chat model
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.5, max_completion_tokens = 100)
response = llm.invoke("what is Transformer in two lines?")
print(response.content)