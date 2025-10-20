from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def findAll():
    return db.carros, 200

@app.route("/carros/<int:id>", methods=["GET"])
def findById(id: int):
    for car in db.carros:
        if car['id'] == id:
            return car, 200
    
    info = {'title': "Nenhuma carro encontrado", "status": 404}
    return info, 404

@app.route("/carros", methods=['POST'])
def cadastra():
    info = request.json
    db.carros.append(info)
    return info, 201

@app.route("/carros", methods=['PUT'])
def altera():
    info = request.json
    i = 0 
    while i < len(db.carros):
        car = db.carros[i]
        if car['id'] == info['id']:
            db.carros[i] = info
            return (info, 200)
        i = i + 1        
    erro = {"status": 400, 'title': 'erro na hora de subtituir o veiculo na lista original'}
    return erro, 400



app.run(debug=True)
