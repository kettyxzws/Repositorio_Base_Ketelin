import requests

try: 
    url = "https://www.tiktok.com/"
    resposta = requests.get(url)
    print(resposta.status_code)

    if resposta<=299:
        print("link existente")
    else:
        print("link inexistente")
except:

    print("erro")
