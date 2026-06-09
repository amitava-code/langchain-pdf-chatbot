# 📄 PDF Chatbot (LLM-based Q&A)

A simple PDF-based question answering system built using **LangChain** and **Google Gemini**.
This project demonstrates how to extract content from a PDF and use it as context for an LLM to answer user queries.

---

## 🚀 Features

* 📥 Load and parse PDF using `PyPDFLoader`
* 🧠 Use **Gemini (gemini-2.5-flash)** for natural language understanding
* 💬 Ask questions based on PDF content
* ⚡ Simple and lightweight implementation (no vector DB yet)

---

# 💻 Tech Stack:

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![PyPDF](https://img.shields.io/badge/PyPDF-FF6F00?style=for-the-badge)

---


## 🧠 How It Works

1. Load PDF using `PyPDFLoader`
2. Extract full text content
3. Pass content into `SystemMessage` as context
4. Ask question using `HumanMessage`
5. LLM generates answer based on provided document

---

## 💻 Code Overview

```python
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import SystemMessage, HumanMessage

loader = PyPDFLoader('./fullstack_guide.pdf', mode="single")
docs = loader.load()

story = docs[0].page_content

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response = model.invoke([
    SystemMessage(f"<story>{story}</story>"),
    HumanMessage("How AI is changing Full-stack development?")
])

print(response.text)
```
---


## ⚠️ Limitations

* ❌ No chunking (large PDFs may hit token limits)
* ❌ No embeddings or vector search
* ❌ Entire PDF is passed to the model (not scalable)


---

## 📌 Key Learning

This project demonstrates a **naive RAG approach** using prompt injection, which is a stepping stone toward building production-grade retrieval systems.

---

## 🤝 Contributing

Feel free to fork the repo and improve the project.

---

## ⭐ Support

If you found this helpful, give it a ⭐ on GitHub!


