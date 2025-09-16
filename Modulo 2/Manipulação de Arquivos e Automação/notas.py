import csv

arquivo_csv=open("dados2.csv")
leitor= csv.DictReader(arquivo_csv)

for linha in leitor:
    print(linha["nome"])
print("--------------------")

import csv  

arquivo_csv=open("dados2.csv")
leitor= csv.DictReader(arquivo_csv)

for linha in leitor:
    if linha["nota"] >= "7.0":
        print(linha)
print("---------------------")

import csv

notas= []
with open("dados2.csv","r",newline="")as arquivo:
    leitor=csv.DictReader(arquivo)
    for linha in leitor:
        notas.append(float(linha["nota"]))

media= sum(notas)/len(notas)
print("media da turma:", round(media,2))

import csv
with open("dados2.csv","a",newline="") as arquivo:
    escritor=csv.writer(arquivo)
    escritor.writerow(["Samira","18","8.0"])

            
