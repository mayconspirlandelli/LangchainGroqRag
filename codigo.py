from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv('GROQ_API_KEY')

# Aqui é uma lista de mensagens fixas
mensagens = [
    SystemMessage("Traduza o texto para ingles"),
    HumanMessage("Se inscreva no canal do INF UFG no YouTube")
]

model = init_chat_model("llama3-8b-8192", model_provider="groq")
parser = StrOutputParser()
chain = model | parser

resposta = model.invoke(mensagens)
texto = parser.invoke(resposta)
texto = chain.invoke(mensagens)
print(texto)


#AGora vamos montar um chat com um template de mensagens flexiveis e parametrizadas.
template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])

# print(template_mensagem.invoke({"idioma": "espanhol", 
                        #   "texto": "Faça parte do instituto de informatica"}))


chain = template_mensagem | model | parser
texto = chain.invoke({"idioma": "espanhol", 
                           "texto": "Faça parte do instituto de informatica"})
print(texto)
                      

#Esse template ira receber uma lista de produtos cuja a saída será em formato JSON.
template2 = ChatPromptTemplate.from_messages([
    ("system", "Escreva o texto em formato de {formato}"),
    ("user", "{texto}"),
])                      

chain = template2 | model | parser
texto = chain.invoke({"formato": "JSON", 
                           "texto": "produto: arroz, valor: 10,00, quantidade: 3, produto: açucuar, valor:5,99, quantidade:5 "})
print(texto)