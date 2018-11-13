import time
import random

from listogram import Listogram


class Sentence(object):

    def __init__(self, histogram):
        self.change_histogram(histogram)

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
        accumalator = 0
        random_number = random.randint(1, self.histogram.tokens)
        if self.is_listogram:
            for word in self.histogram:
                accumalator = accumalator + word[1]
                if accumalator >= random_number:
                    return word[0]


if __name__ == "__main__":
    histogram = Listogram("Red fish blue fish one fish two fish.".split(' '))
    sentence = Sentence(histogram)
    print(sentence.get_sentence(50, True))
