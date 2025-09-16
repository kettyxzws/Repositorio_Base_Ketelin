lista_supermercado =[]
opção =  4
while opção != 0:
     opção = int(input("digite os deseja fazer: \n \n1 - adicionar produto n\ 2 - ver produtos n\ 3 - modificar n\ 4 - remover produto \n 5 - apagar lista"))
     if opção == 1:
         novo = input("digite o item novo \n")
         lista_supermercado.append(novo)
         print(f"produto adicionado")
         try:
          quantidade = int(input("qual o número de itens? \n"))
         except:
          print("quantidade incorreta \n")
     elif opção  == 2:
         print(lista_supermercado)
     elif opção == 3:
            antigo = input(" coloque o produto que deseja modificar: \n ")
            if antigo in lista_supermercado:
              novo = input ("coloque o novo produto: \n ")
              index = lista_supermercado.index(antigo)
              lista_supermercado[index]= novo
              print(f" lista atualizada: \n {lista_supermercado}") 
            else:
              print(" produto não encontrado")
     elif opção == 4:
      remover = input(" coloque o produto para remover \n")
      lista_supermercado.remove(remover)
      print(f"{remover} foi removido")
     elif opção == 5:
      lista_supermercado.clear()
      print(f" \nlista deletada \n")
    
