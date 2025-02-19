from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
chave_api = os.getenv('GROQ_API_KEY')

mensagens = [
    SystemMessage("Traduza o texto para inglês"),
    HumanMessage("Se inscreva no canal do INF UFG no YouTube")
]

model = init_chat_model("llama3-8b-8192", model_provider="groq")
parser = StrOutputParser()

resposta = model.invoke(mensagens)
print(resposta)

texto = parser.invoke(resposta)

#print(texto)