from flask import Flask, jsonify, request

#app = Flask(__name__)
app = Flask("Projeto API Render")

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

app.run(debug=True)