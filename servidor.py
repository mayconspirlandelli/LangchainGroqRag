from codigo import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="Nosso API que acessa uma LLM customizada"
)


add_routes(app, chain, path="/tradutor")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

