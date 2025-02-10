from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home_route():
    return 'Hey I am running on a docker container!'


app.run(host='0.0.0.0', port=8080)
