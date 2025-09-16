def clima():
    clima=float(input("digite quantos graus está fazendo hoje:"))

    if clima <=9:
        print("hoje está frio")
    elif clima <=20:
        print("hoje está nublado")
    elif clima <=40:
        print("hoje está calor")
clima()
