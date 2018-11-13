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
    return sentence.get_sentence(count)
