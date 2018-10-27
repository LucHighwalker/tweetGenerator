import os
import time
import getch

words = [line.rstrip('\n')
         for line in open('./words.txt')]

possibilities = list()
sentence = ''
current_word = ''

cursor_timing = 1
cursor_switched = time.time()
cursor = '|'


def display():
    global possibilities
    global sentence
    global cursor_timing
    global cursor_switched
    global current_word
    global cursor

    os.system('cls' if os.name == 'nt' else 'clear')

    if time.time() - cursor_switched >= cursor_timing:
        if cursor == '':
            cursor = '|'
        else:
            cursor = ''

    word_count = 0
    disp_possible = ''
    for word in possibilities:
        if word_count < 5:
            disp_possible = '{}{} '.format(disp_possible, word)
            word_count = word_count + 1
        else:
            break
    
    display = '{}\n\n{}{}{}\n\n\n'.format(disp_possible, sentence, current_word, cursor)
    print(display)


def get_possibilities(letter):
    global possibilities
    global current_word

    if len(possibilities) == 0:
        word_list = words
    else:
        word_list = possibilities

    new_possibilites = list()

    for word in word_list:
        if len(word) >= len(current_word):
            if word[len(current_word) - 1] == letter:
                new_possibilites.append(word)

    possibilities = new_possibilites


def user_input():
    global possibilities
    global sentence
    global current_word

    try:
        user_input = getch.getch()
        if user_input == ' ':
            if len(possibilities) > 0:
                if current_word != possibilities[0]:
                    current_word = possibilities[0]
            possibilities = list()
            sentence = '{}{} '.format(sentence, current_word)
            current_word = ''
        else:
            current_word = '{}{}'.format(current_word, user_input)
            get_possibilities(user_input)
        return True

    except EOFError:
        return False


if __name__ == '__main__':
    running = True
    display()
    while running:
        user_input()
        display()
