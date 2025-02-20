from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remota.invoke({"idioma": "portugues",
                                "texto": "Faça parte do instituto de informatica"})
print(texto)