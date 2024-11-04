import requests
from pprint import pprint  # Para exibir os dados de forma mais organizada

API = 'http://127.0.0.1:5000'

def get_produtos():
    response = requests.get(f"{API}/produtos")
    if response.status_code == 200:
        return response.json()  # Retorna os dados no formato JSON (lista de produtos)
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []

# Recebe os produtos e os exibe de forma organizada
produtos = get_produtos()
if produtos:
    for produto in produtos:
        print("Produto:")
        pprint(produto)  # Exibe cada produto formatado
else:
    print("Nenhum produto encontrado.")
