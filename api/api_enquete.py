from flask import Flask, jsonify, request

pergunta = {
    "numero": 1,
    "texto": "Brasil é favorito para ganhar a Copa?",
    "tipo": "UNICA",
    "alternativas": ['Sim', 'Não']
}

app = Flask(__name__)

lista_perguntas = []
lista_respostas = []

@app.route("/pergunta", methods=['POST'])
def cadastra_pergunta():
    pergunta = request.json
    #deveria verificar se pergunta é um json que representa a pergunta
    #sendo um formato correto, chamo a funcao que grava a pergunta no banco dados

    lista_perguntas.append(pergunta)

    #try:
    #    banco.cadastra_pergunta_oracle(pergunta)
    #except Exception as e:
    #    info = {'erro': str(e)}
    #    return info, 400
    
    return (jsonify(pergunta), 201)


@app.route("/pergunta", methods=['GET'])
def consulta_perguntas():
    if len(lista_perguntas) == 0:
        return lista_perguntas, 404
    else:
        return jsonify(lista_perguntas), 200

@app.route("/resposta", methods=['POST'])
def cadastra_resposta():
    info = request.json
    #deveria verificar se info é um json que representa uma resposta
    lista_respostas.append(info)
    return jsonify(info), 201

app.run(debug=True)