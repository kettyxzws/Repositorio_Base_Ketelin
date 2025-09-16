import json

dados_json='{ "nome":"samira","idade":15,"cidade":"São Paulo" }'
dados_python = json.loads(dados_json)

print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["cidade"])
print("--------------------")

import json

dados_json = '{"produto":"Caderno", "preco": 12.5, "estoque": 30}'
dados_python=json.loads(dados_json)

print(dados_python["produto"])
print(dados_python["preco"])
print("----------------------")


import json

dados_json= '{"nome": "Lucas","idade": 16,"aprovado":"True"}'
dados_python=json.loads(dados_json)

print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["aprovado"])
 
import json

dados ='{"filme": "Matrix","ano": 1999, "genero": "Ficção Científica"}'

