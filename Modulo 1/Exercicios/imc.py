nome = str(input("Qual é o seu nome?"))
peso = float(input("Qual é o seu peso?"))
altura = float(input("Qual é a sua altura?"))

IMC = peso / (altura * altura)

if IMC <=18.5:
       print("abaixo do peso")
elif IMC <=24.9:
       print("peso normal")
elif IMC >=29.9:
       print("sobrepeso")
elif IMC <=34.9:
      print("Obesidade grau 1")
elif IMC <=39.9:
      print("Obesidade grau 2")
else:
      print("Obesidade grau 3(mórbida)")
