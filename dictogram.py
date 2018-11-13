#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            previous_word = ''
            for word in word_list:
                self.add_count(word, previous_word)
                previous_word = word

    def add_count(self, word, previous_word, count=1):
        """Increase frequency count of given word by given count amount."""
        if previous_word != '':
            try:
                dicto = self[previous_word]
            except KeyError:
                dicto = {}
            try:
                word_count = dicto[word]
                dicto[word] = word_count + count
            except KeyError:
                dicto[word] = count
            self[previous_word] = dicto

        # if previous_word != '':
        #     dicto = self.get(previous_word, {})
        #     word_count = dicto[previous_word].get(word, 0)
        #     if word_count > 0:
        #         dicto[previous_word][word] = word_count + count
        #     else:
        #         dicto[previous_word][word] = count
        #     self[previous_word] = dicto
        # try:
        #     if previous_word != '':
        #         self[previous_word][word] = self[previous_word][word] + count
        #         self.tokens = self.tokens + count
        # except KeyError:
        #     self[previous_word] = {}
        #     self[previous_word][word] = count
        #     self.types = self.types + 1
        #     self.tokens = self.tokens + count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        try:
            return self[word]
        except KeyError:
            return 0


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
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
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
