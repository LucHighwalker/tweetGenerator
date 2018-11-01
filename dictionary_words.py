import random
import time
import sys

start_time = time.time()

words = [line.rstrip('\n')
         for line in open('/usr/share/dict/cracklib-small')]


def generate_sentence(word_count):
    sentence = list()
    while len(sentence) < int(word_count):
        rand_word = random.choice(words)
        sentence.append(rand_word)
    return ' '.join(sentence)


if __name__ == "__main__":
    print(generate_sentence(sys.argv[1]))
    print("\n\ngenerated in %s seconds" % (time.time() - start_time))
