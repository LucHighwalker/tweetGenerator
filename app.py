from flask import Flask
import stochastic

app = Flask(__name__)


@app.route('/')
def hello_world():
    histogram = stochastic.open_histogram('histograms/histogram.txt')
    return stochastic.generate_sentence(histogram, 10)
