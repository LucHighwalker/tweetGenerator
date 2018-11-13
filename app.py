from flask import Flask, request

from listogram import Listogram
from file_parser import File_Parser
from sentence import Sentence

app = Flask(__name__)


@app.route('/')
def hello_world():
    file_parser = File_Parser('./steamman.txt')
    word_list = file_parser.parsed_file
    listogram = Listogram(word_list)
    sentence = Sentence(listogram)

    count = request.args.get('num', default=10, type=int)
    return sentence.get_sentence(count)
