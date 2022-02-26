from flask import Flask, jsonify


app = Flask(__name__)

languages = ['Python', 'JavaScript', 'Java']


@app.route('/', methods=['GET'])
def get():
    return { "languages": languages }
