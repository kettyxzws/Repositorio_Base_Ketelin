import csv

arquivo_csv=open("dados.csv")
leitor= csv.DictReader(arquivo_csv)

for linha in leitor:
    if linha ["Marca"]== "Ford":
        print(linha)

import csv  

arquivo_csv=open("dados.csv")
leitor= csv.DictReader(arquivo_csv)
print("------")
for linha in leitor:
    if linha ["Ano"]== "2020":
        print(linha)

import csv  

arquivo_csv=open("dados.csv")
leitor= csv.DictReader(arquivo_csv)
print("------")
 
for linha in leitor:
    preco=int(linha["Preco"])

    if preco < 50000:
        print(linha)

import csv
with open("dados.csv","a",newline="") as arquivo:
    escritor=csv.writer(arquivo)
    escritor.writerow(["Nathalia","Bea","lorrani"])
