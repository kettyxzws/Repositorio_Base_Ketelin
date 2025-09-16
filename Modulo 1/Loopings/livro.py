def cadastrar():
    item=input("digite o livro que irá adicionar: ")
    print(f" {item} cadastro com sucesso")

def valor():
    valor=float(input("quanto custa o livro:"))
    print("livro comprado com sucesso")
    
opção = 0
while opção !=3:
    opção=int(input("digite a opção que deseja: \n 1- adicionar o livro \n 2-ver livro \n 3-sair"))
    if opção == 1:
        cadastrar()
    elif opção ==2:
        valor()
    elif opção ==3:
        print("voce saiu com sucesso")

