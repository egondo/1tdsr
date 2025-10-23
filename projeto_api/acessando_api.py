import requests

url = "https://fiap-tdsr.onrender.com/enderecos"
response = requests.get(url)
if response.status_code == 200:
    enderecos = response.json()
    for endereco in enderecos:
        print(f"{endereco['logradouro']}, {endereco['numero']} - {endereco['bairro']}")


        