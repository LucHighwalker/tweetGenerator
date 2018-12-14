import flask

from dictogram import Dictogram
from file_parser import File_Parser
from sentence import Sentence

app = flask.Flask(__name__)

file = File_Parser('./steamman.txt')
dictogram = Dictogram(file.parsed_file, 4)
sentence = Sentence(dictogram, 4)


@app.route('/', methods=['GET'])
def hello_world():
    count = flask.request.args.get('num', default=10, type=int)
    benchmark = flask.request.args.get('bench', default=False, type=bool)

    resp = sentence.get_sentence(count, bool(benchmark))

    response = flask.jsonify({'resp': resp})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
