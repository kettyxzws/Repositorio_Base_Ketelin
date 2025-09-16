opção = 7

numero = int(input(" coloque um numero impar"))
numero = int(input(" coloque um numero par"))
while opção !=2:
    numero = int(input("adicione um numero inteiro"))
    if numero %2==0:
        print(f" {numero} é par!")
else:
    print(f"{numero} é impar ")
    opção = int(input("digite 1 para tentar repetir?\n 2 para sair"))
