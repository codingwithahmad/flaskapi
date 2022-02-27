from flask import Flask, request


app = Flask(__name__)

languages = ['Python', 'JavaScript', 'Java']

@app.route('/', methods=['POST'])
def post_language():
    arg = request.get_json()
    print(arg)
    if arg.get('name'):
        languages.append(arg['name'])
        return {}, 201
    return {}


@app.route('/', methods=['GET'])
def get_languages():
    return { "languages": languages }


@app.route('/<int:index>', methods=['GET'])
def get_language(index):
    try:
        return {'language': languages[index]}
    except IndexError as e:
        return {}, 404
