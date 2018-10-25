import os
import getch

words = [line.rstrip('\n')
         for line in open('./words.txt')]

possibilities = list()
sentence = ''
current_word = ''


def display():
    global possibilities
    global sentence
    global current_word

    os.system('cls' if os.name == 'nt' else 'clear')

    word_count = 0
    disp_possible = ''
    for word in possibilities:
        if word_count < 5:
            disp_possible = '{}{} '.format(disp_possible, word)
            word_count = word_count + 1
        else:
            break
    
    display = '{}\n\n{}{}'.format(disp_possible, sentence, current_word)
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
        if user_input():
            display()
