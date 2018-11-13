from flask import Flask, request

from dictogram import Dictogram
from file_parser import File_Parser
from sentence import Sentence

app = Flask(__name__)


@app.route('/')
def hello_world():
    file = File_Parser('./steamman.txt')
    histogram = Dictogram(file.parsed_file)
    sentence = Sentence(histogram)

    count = request.args.get('num', default=10, type=int)
    benchmark = request.args.get('bench', default=False, type=bool)
    sentence = sentence.get_sentence(count, bool(benchmark))
    if benchmark:
        return "generation time: {}\n\n{}".format(sentence[0], sentence[1])
    return sentence
