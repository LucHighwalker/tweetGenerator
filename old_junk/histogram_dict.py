import time

start_time = time.time()


def read_file():
    lines = [line.rstrip('\n').strip(' ')
             for line in open('./steamman.txt')]
    return lines


def add_word(words, word):
    try:
        value = words[word]
        words[word] = value + 1
    except KeyError:
        words[word] = 1
    return words


def generate_histogram(lines):
    words = {}
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
