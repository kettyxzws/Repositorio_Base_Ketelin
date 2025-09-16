nome = input("digite seu nome")
email = input("digite seu email")

arquivo = open("pessoa.txt" , "a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()
