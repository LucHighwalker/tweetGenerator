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
        last_word = sentence_array[-1]
        sentence_array.pop()
        new_sentence = '{}{} '.format(new_sentence, last_word)
    print(new_sentence)
