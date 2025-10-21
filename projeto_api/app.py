from flask import Flask, jsonify, request
import banco

#app = Flask(__name__)
app = Flask("Projeto API Render")

@app.route("/carros", methods=["GET"])
def get_carros():
    return banco.consulta_carros(), 200

@app.route("/cartao", methods=['GET'])
def get_card():
    cartao = {
        "nome": "José Carlos",
        "email": 'zecarlos@fiap.com.br',
        "departamento": "RH",
        "telefone": "(11) 4528-9087",
        "cargo": "analista de recursos humanos"
    }
    return cartao, 200


@app.route("/enderecos", methods=['GET'])
def get_adress() -> list:
    lista = [
        {
            "logradouro": "Av Paulista",
            "numero": 1106,
            "bairro": "Bela Vista"
        },
        {
            "logradouro": "Av Lins de Vasconcelos",
            "numero": 1222,
            "bairro": "Aclimação"
        }
    ]
    return lista, 200

app.run(debug=True)