from langchain_ollama import ChatOllama, OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Conectando com o modelo rodando localmente no Ollama
model = OllamaLLM(model="llama3")

# messages = [
#   SystemMessage('Traduza o texto a seguir:'),
#   HumanMessage("Explique o que é aprendizado de máquina.")
# ]

# parser = StrOutputParser()

# chain = model | parser

message_template = ChatPromptTemplate.from_messages([
  ("system", "Responda as perguntas na lingua portuguesa (Brasil)"),
  ("user", "{question}")
])

chain = message_template | model

# print(chain.invoke({"question": "italiano", "texto": "Se inscrevam no canal do youtube!"}))

# Enviando uma mensagem
# response = model.invoke(messages)

# print(response)
