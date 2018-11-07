from flask import Flask, request
import stochastic

app = Flask(__name__)


@app.route('/')
def hello_world():
    histogram = stochastic.open_histogram('histograms/histogram.txt')
    count = request.args.get('num', default=10, type=int)
    return stochastic.generate_sentence(histogram, count)
