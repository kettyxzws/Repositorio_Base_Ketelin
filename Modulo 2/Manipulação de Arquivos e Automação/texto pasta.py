import os
import flet as ft
texto_pasta=""

def main(page: ft.Page):
    page.title = "Interface com OS"
    page.theme_mode = "dark"
    
    # Função para criar pastas
    def criar_pasta(e):
        global texto_pasta
        texto_pasta = texto_recebido.value
        try:
            os.mkdir(texto_pasta)
            informativo.value = f"Pasta criada: '{texto_pasta}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto_pasta}' já existe."
        page.update()
    
    # Função para criar arquivos
    def criar_arquivo(e):
        global texto
        if texto_pasta=="":
            texto= texto_recebido.value
            open(texto,"w").close()
            informativo.value = f"arquivo criado:'{texto}'"
        else:
            texto= texto_recebido.value
            open(f"{texto_pasta}/{texto}","w").close()

        page.update()

    def criar_lista(e):
            arquivo=os.listdir(texto_pasta)
            for item in arquivo: 
                print(arquivo)
            informativo.value = f"arquivos: {arquivo}"
            page.update()
         
    def criar_renomear(e):
        global texto_pasta
        texto_antigo= texto
        if texto_pasta=="":
            texto_novo= texto_recebido.value
            os.rename(f"{texto_pasta}/{texto_novo}",f"{texto_pasta}/{texto_novo}")
            informativo.value = f"renomeado: {texto_antigo} a {texto_novo}"
        else:
            texto_novo= texto_recebido.value
            os.rename(f"{texto_pasta}/{texto_antigo}",f"{texto_pasta}/{texto_novo}")
            informativo.value=f"arquivo renomeado de '{texto_antigo} para {texto_novo}"
            page.update


    def criar_apagar(e):
        texto=texto_recebido.value
        if texto_pasta=="":
            os.remove(texto)
            informativo.value=f"remover:{texto}"
        else:
            os.remove(f"{texto_pasta}/{texto}")
            informativo.value=f"arquivo removido {texto_pasta}/{texto}"
            page.update
       
            
            


    # Campos e botões
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo)
    botao_lista = ft.ElevatedButton("LISTAR ARQUIVO", bgcolor="BLUE", color="BLACK", width=200, on_click=criar_lista)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVO", bgcolor="RED", color="WHITA", width=200, on_click=criar_renomear)
    botao_apagar = ft.ElevatedButton("APAGAR ARQUIVO", bgcolor="GREEN", color="WHITE", width=200, on_click=criar_apagar)
    informativo = ft.Text("", size=20, color="white")


    # Layout
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo], alignment="center"),
        ft.Row([botao_lista], alignment="center"),
        ft.Row([botao_renomear], alignment="center"),
        ft.Row([botao_apagar], alignment="center"),
        ft.Row([informativo], alignment="center"))

ft.app(target=main)
