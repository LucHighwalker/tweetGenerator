import time

start_time = time.time()


def read_file():
    lines = [line.rstrip('\n').strip(' ')
             for line in open('./steamman.txt')]
    return lines


def add_word(words, word):
    word_found = False
    word_index = 0
    for word_array in words:
        if word_array[0] == word:
            occurence = word_array[1] + 1
            words[word_index] = (word, occurence)
            word_found = True
            break
        word_index = word_index + 1
    if not word_found:
        words.append((word, 1))
    return words


def generate_histogram(lines):
    words = []
    for line in lines:
        words_in_line = line.split(' ')
        for word in words_in_line:
            if len(word) > 0:
                if word != 'I':
                    word = word.lower()
                # gets rid of all unnecessary characters
                word = word.strip("'")
                word = word.replace('.', '').replace(',', '').replace(
                    '!', '').replace('?', '').replace(':', '').replace(
                        ';', '').replace('(', '').replace(')', '')
                words = add_word(words, word)
    return words


if __name__ == "__main__":
    lines = read_file()
    print(generate_histogram(lines))
    print("\n\nGenerated in {} seconds".format(time.time() - start_time))
