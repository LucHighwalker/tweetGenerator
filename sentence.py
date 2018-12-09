import time
import random

# from listogram import Listogram
from dictogram import Dictogram
# from markov import Markov
from file_parser import File_Parser

from collections import deque


class Sentence(object):

    def __init__(self, histogram, order=2):
        self.change_histogram(histogram)
        self.queue = deque(maxlen=order)

    def change_histogram(self, histogram):
        '''Sets a new histofram'''
        self.histogram = histogram
        if isinstance(histogram, list):
            self.is_listogram = True
        else:
            self.is_listogram = False

    def get_sentence(self, length, benchmark=False):
        '''Generates a sentence of a given length. If benchmarking
        is set to true, returns a list containing sentence and
        generation time. Otherwise, only returns a sentence.'''
        if benchmark:
            start_time = time.time()

        sentence = self._generate_sentence(length)

        # If benchmarking, returns list with sentence string and
        # generation time. Otherwise, returns sentence string.
        if benchmark:
            # sentence = ' '.join(sentence)
            generation_time = time.time() - start_time
            return [generation_time, ' '.join(sentence)]
        else:
            return ' '.join(sentence)

    def _generate_sentence(self, length):
        sentence = []
        while len(sentence) < length:
            random_word = self._get_random_word()
            sentence.append(random_word)
        return sentence

    def _get_random_word(self):
        if len(self.queue) == 0:
            # TODO: get proper starting points.
            for key, _ in self.histogram.items():
                queue = key.split('-,-')
                for word in queue:
                    self.queue.append(word)
                return key
        else:
            key = '-,-'.join(self.queue)
            histogram = self.histogram[key][1]

            random_num = random.randint(1, histogram.types)
            accumalator = 0
            for key, val in histogram.items():
                accumalator = accumalator + val
                if random_num <= accumalator:
                    self.queue.append(key)
                    return key


if __name__ == "__main__":
    file = File_Parser('./steamman.txt')
    # markov = Markov(file.parsed_file)
    histogram = Dictogram(file.parsed_file, 3)
    # print("hsitogram: {}".format(histogram)
    sentence = Sentence(histogram, 3)
    print(sentence.get_sentence(50, True))
