from teste import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Integração da LLM Ollama para responder perguntas!", description="")

add_routes(app, runnable=chain, path='/tradutor')

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host='localhost', port=8000)