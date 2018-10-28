import sys
import random
import time

lines = list()


def open_file(file):
    global lines
    lines = [line.rstrip('\n')
             for line in open(file)]


def generate_sentence(count):
    start_time = time.time()
    sentence = list()
    iterations = 0
    while len(sentence) < int(count):
        iterations = iterations + 1
        random_line = random.choice(lines).split(' ')
        random_word = random_line[0]
        word_chance = int(random_line[1])
        rand_chance = random.random() * 4200
        if rand_chance < word_chance:
            sentence.append(random_word)
    generation_time = time.time() - start_time
    print('generated sentence in {} seconds with {} iterations'.format(
        generation_time, iterations))
    return ' '.join(sentence)


if __name__ == "__main__":
    params = sys.argv[1:]
    open_file(params[0])
    sentence = generate_sentence(params[1])
    print(sentence)
