from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import SystemMessage,HumanMessage

loader = PyPDFLoader('./fullstack_guide.pdf', mode="single")

docs = loader.load()

story = (docs[0].page_content)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response = model.invoke([
    SystemMessage("<story>" + story + "<story>"),
    HumanMessage("How AI is changing Full-stack development ?")
])

print(response.text)