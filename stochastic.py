import sys
import random
import time

histogram = {}
keys = list()


def open_file(file):
    lines = [line.rstrip('\n')
             for line in open(file)]
    for line in lines:
        word_value = line.split(' ')
        keys.append(word_value[0])
        histogram[word_value[0]] = int(word_value[1])


def generate_sentence(count):
    start_time = time.time()
    sentence = list()
    iterations = 0
    while len(sentence) < int(count):
        iterations = iterations + 1
        random_word = random.choice(keys)
        word_chance = histogram[random_word]
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
