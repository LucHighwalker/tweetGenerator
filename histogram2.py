import time

lines = [line.rstrip('\n')
         for line in open('./steamman.txt')]


words = []

preceeding_word = ''


def find_word_index(word):
    global words

    word_index = 0
    word_found = False
    for word_o in words:
        if word_o.word == word:
            word_found = True
            break
        word_index = word_index + 1

    if word_found:
        return word_index
    else:
        return -1


def addWord(word):
    global words
    global preceeding_word

    word_index = find_word_index(word)

    if word_index != -1:
        this_word = words[word_index]
        this_word.occurrence = this_word.occurrence + 1
        words[word_index] = this_word
        if preceeding_word != '':
            preceeding_index = find_word_index(preceeding_word)
            preceeding_this_word = words[preceeding_index]
            if word not in preceeding_this_word.next_words:
                preceeding_this_word.next_words.append(word)

    else:
        class New_Word:
            pass
        New_Word.word = word
        New_Word.occurrence = 1
        New_Word.next_words = []
        new_word = New_Word()
        words.append(new_word)


def generate_histogram():
    global lines
    global preceeding_word

    for line in lines:
        words_in_line = line.split(' ')
        for word in words_in_line:
            if len(word) > 0:
                if word != 'I':
                    word = word.lower()
                # gets rid of all unnecessary characters
                word = word.strip("'")

                end_sentence = False
                if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
                    end_sentence = True

                word = word.replace('.', '').replace(',', '').replace(
                    '!', '').replace('?', '').replace(':', '').replace(
                        ';', '').replace('(', '').replace(')', '')

                addWord(word)
                if end_sentence:
                    preceeding_word = ''
                else:
                    preceeding_word = word


def write_to_file():
    global words

    file = open("histograms/{}.txt".format(time.time()), "w+")
    for word in words:
        line = "{} {}".format(word.word, word.occurrence)
        for next_word in word.next_words:
            line = "{} {}".format(line, next_word)
        line = "{}\n".format(line)
        file.write(line)


if __name__ == "__main__":
    generate_histogram()
    write_to_file()
