import flet as ft
import csv


def main(page:ft.Page):
    page.title="cadastro Login"
    page.theme_mode="dark"

    def clique(e):
        valor_login=texto_login.value
        valor_senha=texto_senha.value
        print(valor_login,valor_senha)
    
        with open("relatorios\dados3.csv","a",newline="") as arquivo:
            escritor=csv.writer(arquivo)
            escritor.writerow([valor_login,valor_senha])
    

    texto_login=ft.TextField(label="login",border_color="Red",focused_border_color="Blue")
    texto_senha=ft.TextField(label="senha",password=True,can_reveal_password=True)

    botao=ft.ElevatedButton("cadastro",on_click=clique)

    page.add(texto_login,texto_senha,botao)

ft.app(target=main)
