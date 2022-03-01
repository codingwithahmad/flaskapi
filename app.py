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


@app.route('/<int:index>', methods=['PUT'])
def modify_language(index):
    arg = request.get_json()
    if arg.get('name'):
        try:
            languages[index] = arg['name']
            return {}, 204
        except IndexError:
            return {}, 404
    return {}, 400

@app.route('/<int:index>', methods=['DELETE'])
def delete_language(index):
    try:
        del languages[index]
        return {}, 204
    except IndexError:
        return {}, 404
