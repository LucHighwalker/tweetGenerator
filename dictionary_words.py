import random
import time
import sys


class Words(object):
    def __init__(self, optimization_count):
        self.word_bank = list()
        self.words = [line.rstrip('\n')
                      for line in open('/usr/share/dict/cracklib-small')]
        # self.optimizer(int(optimization_count))

    # trash and only slows it down
    def optimizer(self, optimization_count):
        word_count = len(self.words)
        block_size = word_count // optimization_count

        current_block = 0
        word_index = 0
        self.word_bank.append(list())
        while word_count > 0:
            self.word_bank[current_block].append(self.words[word_index])
            word_count = word_count - 1
            word_index = word_index + 1
            if len(self.word_bank[current_block]) == block_size:
                current_block = current_block + 1
                self.word_bank.append(list())

    def generate_sentence(self, word_count):
        sentence = list()
        # word_bank = random.choice(self.word_bank)
        while len(sentence) < int(word_count):
            rand_word = random.choice(self.words)
            sentence.append(rand_word)
        return sentence


if __name__ == "__main__":
    start_time = time.time()
    params = sys.argv[1:]
    word_count = params[0]
    if len(params) > 1:
        optimization_count = params[1]
    else:
        optimization_count = 4
    words = Words(optimization_count)
    print(words.generate_sentence(word_count))
    print("generated in %s seconds" % (time.time() - start_time))
