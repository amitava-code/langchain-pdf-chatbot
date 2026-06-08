from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./fullstack_guide.pdf', mode="single")

docs = loader.load()

print(docs[0].page_content)

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# response = model.invoke("what is full-stack ?")

# print(response.text)