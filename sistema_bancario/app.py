from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import negocio

app = Flask("Sistema de lançamento")
CORS(app, origins = " http://127.0.0.1:5000")


@app.route("/contas")
@cross_origin()
def get_contas():
    return negocio.recupera_contas()


app.run(debug=True)