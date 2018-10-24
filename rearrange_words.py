import random
import os


def user_input(prompt):
    try:
        user_input = input(prompt)
        os.system('cls' if os.name == 'nt' else 'clear')
        return user_input

    except EOFError:
        return ''


if __name__ == "__main__":
    sentence = user_input('input a sentence: ')
    sentence_array = sentence.split(' ')
    new_sentence = ''
    while len(sentence_array) > 0:
        rand_word = random.choice(sentence_array)
        sentence_array.remove(rand_word)
        new_sentence = '{}{} '.format(new_sentence, rand_word)
    print(new_sentence)
