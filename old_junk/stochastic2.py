import sys
import random
import time

histogram = []


def find_word(find_word):
    for word in histogram:
        if word.word == find_word:
            return word
    return 0


def open_file(file):
    lines = [line.rstrip('\n')
             for line in open(file)]
    for line in lines:
        word_value = line.split(' ')
        word = word_value[0]
        occurence = int(word_value[1])
        next_words = word_value[2:]

        class New_Word:
            pass
        New_Word.word = word
        New_Word.occurence = occurence
        New_Word.next_words = next_words
        new_word = New_Word()
        histogram.append(new_word)


def generate_sentence(count):
    start_time = time.time()
    sentence = []
    next_words = []
    sentence_ended = True

    iterations = 0
    while len(sentence) < count:
        iterations = iterations + 1
        if len(next_words) > 0:
            rand_next_word = random.choice(next_words)
            random_word = find_word(rand_next_word)
        else:
            random_word = random.choice(histogram)

        word_chance = random_word.occurence
        random_chance = random.random() * len(histogram)
        if random_chance < word_chance:
            word = random_word.word
            if sentence_ended:
                word = word.capitalize()
                sentence_ended = False
            next_words = random_word.next_words
            if len(next_words) == 0:
                word = "{}.".format(word)
                sentence_ended = True
            sentence.append(word)

    generation_time = time.time() - start_time
    print('generated sentence in {} seconds with {} iterations'.format(
        generation_time, iterations))
    return ' '.join(sentence)


if __name__ == "__main__":
    params = sys.argv[1:]
    open_file(params[0])
    sentence = generate_sentence(int(params[1]))
    print(sentence)
