import re


class Chorpus_Cleaner(object):

    def __init__(self, path=None):
        """If path is given, store parsed data."""
        if path is not None:
            self.parsed_file = self.read_file(path)

    def read_file(self, path):
        """returns a list of all words in the given source."""

        lines = [line.rstrip('\n').strip(' ')
                 for line in open(path)]

        word_list = []
        for line in lines:
            line = re.sub("[?.!]+", " E~N~D S~T~A~R~T ", line)
            line = re.sub("(Chapter [0-9]+)", "", line)
            line = re.re("([A-Za-z]+'[A-Za-z]+)", "", line)
            for word in line.split():
                if word != ' ' and word != '':
                    special_chars = re.findall("[^A-Za-z0-9~]+", word)
                    word = re.sub("[^A-Za-z0-9~]+", "", word)
                    word_list.append(word.lower())
                    if len(special_chars) > 0:
                        for char in special_chars:
                            word_list.append(char)
        return word_list


if __name__ == "__main__":
    file_parser = Chorpus_Cleaner('./steamman.txt')
    print(file_parser.parsed_file)
