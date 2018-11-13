class File_Parser(object):

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
            for word in line.split():
                if word != ' ':
                    word_list.append(word.lower())

        return word_list


if __name__ == "__main__":
    file_parser = File_Parser('./steamman.txt')
    print(file_parser.parsed_file)
