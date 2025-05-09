from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.retriever import retriever

model = OllamaLLM(model="llama3")

template = """
  Você é um assistente de uma empresa de vendas de produtos.
  Seu trabalho é conversar com os clientes e funcionários, consultando a base de conhecimentos da empresa
  e responder conforme a base de dados fornecida no contexto.

  Contexto: {context}

  Pergunta: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
  { "context": retriever, "question": RunnablePassthrough } |
  prompt |
  model
)