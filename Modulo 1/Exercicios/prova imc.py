
nome = str(input("Qual é o seu nome?"))
peso = float(input("Qual é o seu peso"))
altura = float(input("Qual é a sua altura?"))

IMC = peso / (altura*altura)
 
if IMC >=18.5:
    print(f"{nome} está abaixo do peso {IMC}") 
elif IMC >=24.9:
     print(f"{nome} está abaixo o peso normal {IMC}")
elif IMC >=29.9:
     print(f"{nome} está com sobrepeso {IMC}")
elif IMC >=34.9:
     print(f"{nome} está com obesidade grau I {IMC}")
elif IMC >=39.9:
     print(f"{nome} está com obesidade grau II {IMC}") 
else:
     print(f"{nome} está com obesidade grau III (mórbida) {IMC}")
     print("Cuidado com a sua saúde 😥😥")
