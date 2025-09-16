import os
import flet as ft

def main(page:ft.Page):
    page.titte="interface com OS"
    page.theme_mode="dark"

    def criar_pasta(e):
        texto=texto_recebido.value
        os.mkdir(texto)
        
        page.update()

    texto_recebido=ft.TextField(label="fala aí meu🤨")
    botao=ft.ElevatedButton("CRIAR PASTA",bgcolor="BLUE",color="WHITE",width=200,on_click=criar_pasta)
    botaoo=ft.ElevatedButton("CRIAR ARQUIVO",bgcolor="RED",color="WHITE",width=200,on_click=criar_arquivo)
    page.add(ft.Row([texto_recebido],alignment="center"),
            ft.Row([botao],alignment="center"),
            ft.Row([botaoo],alignment="center"))     

ft.app(target=main)



