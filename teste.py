from langchain_ollama import ChatOllama, OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.document_loaders import CSVLoader

# Conectando com o modelo rodando localmente no Ollama
model = OllamaLLM(model="llama3")

message_template = ChatPromptTemplate.from_messages([
  ("system", "Responda as perguntas com base nas informações do contexto: {context}"),
  ("user", "{question}")
])

info = [
  "O papa mais recente é Leão XIV, nascido Robert Francis Prevost, eleito em 8 de maio de 2025 como o 267º pontífice da Igreja Católica. Ele sucede o papa Francisco, falecido em 21 de abril de 2025, após 12 anos de pontificado.",
  "Leão XIV é o primeiro papa nascido nos Estados Unidos, natural de Chicago, e possui também cidadania peruana desde 2015.",
  "ua trajetória inclui décadas de serviço missionário no Peru, onde foi bispo de Chiclayo."
]

loader = CSVLoader("./src/assets/vendas.csv")
document = loader.load()

# source_knowledge = "\n\n".join(info)

# prompt = f"""Use o contexto da base de dados para responder às pergutas!

# Contexto: {source_knowledge}

# Pergunta: {question}
# """

chain = message_template | model

# print(chain.invoke({"question": "italiano", "texto": "Se inscrevam no canal do youtube!"}))

# Enviando uma mensagem
# response = model.invoke(messages)

print(chain.invoke({ "context": document,"question": "Quais os tipos de produtos existentes?" }))
