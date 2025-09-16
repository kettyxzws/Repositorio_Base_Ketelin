opção = 7 

nome_login= input("Digite seu nome de login :")
senha_login = input("Digite sua senha para login : ")
while opção != 2:
    nome_cadastrado =  input("Coloque seu nome de cadastro : ")
    senha_cadastrada = input("Digite sua senha de cadastro: ")

    if nome_login == nome_cadastrado and senha_cadastrada == senha_login :
        print("Bem vindo")


    else:
        print("Errado tente novamente")
        opção = input("Digite 1 para tentar novamente \n 2 para sair")

