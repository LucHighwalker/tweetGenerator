import time

lines = [line.rstrip('\n')
         for line in open('./steamman.txt')]

f = open("histograms/%s.txt" % time.time(), "w+")


words = {}


def addWord(word):
    try:
        value = words[word]
        words[word] = value + 1
    except KeyError:
        words[word] = 1


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
            addWord(word)


for k, v in words.items():
    f.write("%s %s\n" % (k, v))
