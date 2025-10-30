from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import negocio
import traceback

app = Flask("Sistema de lançamento")
CORS(app, origins="http://127.0.0.1:5000")


@app.route("/contas", methods=["GET"])
@cross_origin()
def get_contas():
    return negocio.recupera_contas(), 200

@app.route("/contas/transacao", methods=["POST"])
@cross_origin()
def cadastra_transacao():
    try:
        lancamento = request.json
        negocio.cadastra_transacao(lancamento)
        return lancamento, 201
    except Exception as erro:
        info = {"erro": "Erro no cadastro da transacao"}
        return info, 400

@app.route("/contas/transacao/<int:conta>", methods=["GET"])
@cross_origin()
def recupera_transacoes(conta: int):
    try:
        lista = negocio.recupera_transacoes(conta)
        return lista, 200
    
    except Exception as erro:
        traceback.print_exc()
        info = {"erro": "Erro na recuperacao dos dados"}
        return info, 400



app.run(debug=True)