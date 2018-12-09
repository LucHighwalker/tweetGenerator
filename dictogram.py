#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from collections import deque


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None, markov_order=1, original=True):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        self.queue = deque(maxlen=markov_order)
        self.prev_key = None
        self.is_original = original
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self.queue.append(word)
        key = '-,-'.join(self.queue)
        # TODO: Increase word frequency by count
        try:
            if self.is_original:
                freq_dict = self[key]
                self[key] = (freq_dict[0] + count, freq_dict[1])
            else:
                self[key] = self[key] + count
            self.tokens = self.tokens + count
        except KeyError:
            if self.is_original:
                self[key] = (count, Dictogram(original=False))
            else:
                self[key] = count
            self.types = self.types + 1
            self.tokens = self.tokens + count
            
        if self.is_original is True:
            if self.prev_key is not None:
                self[self.prev_key][1].add_count(word, count)
            # self[self.prev_key][1].add_count(key, count)

        self.prev_key = key

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        try:
            return self[word]
        except KeyError:
            return 0


def print_histogram(word_list, markov_order):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list, markov_order)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments, 1)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word), 1)
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split(), 2)
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split(), 3)


if __name__ == '__main__':
    main()
