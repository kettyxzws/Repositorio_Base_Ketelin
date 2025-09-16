# import csv 

# arquivo_csv = open("dados.csv")
# leitor = csv.DictReader(arquivo_csv)

# for linha in leitor:
#     if linha['Marca'] == "Ford":
#         print(linha) 

# import csv 
# print("----------")
# arquivo_csv = open("dados.csv")
# leitor = csv.DictReader(arquivo_csv)

# for linha in leitor:
#     if linha['Ano'] == "2018":
#         print(linha) 

import csv

with open("dado.csv", "a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["ifood","iphone","maquiagem"]
