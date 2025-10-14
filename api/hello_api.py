from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    info = {"msg": "Hello World!"}
    return info

app.run(debug=True)
