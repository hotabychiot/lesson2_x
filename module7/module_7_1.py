


class WordsFinder:
    def __init__(self, *file):
        self.__all_files = list(file)
        self.__all_words = self.get_all_words()
    def get_all_words(self):
        dictWords = {}
        for nameFile in self.__all_files:
            listWords = []
            with open(nameFile, 'r', encoding='utf-8') as file:
                for line in file:
                    line = self.__cleaning(line, ',', '.', '=', '!', '?', ';', ':', ' - ')
                    line = line.lower()
                    line = line.strip()
                    listWords.extend(line.split())
            dictWords[nameFile] = listWords
        return dictWords
    def find(self, word):
        dictWords = {}
        word = word.lower()
        for i in self.__all_words.items():
            try:
                n = i[1].index(word)
            except ValueError:
                print("Элемент не найден")
                n = -1
            dictWords[i[0]] = n + 1
        return dictWords

    def count(self, word):
        dictWords = {}
        word = word.lower()
        for i in self.__all_words.items():
            dictWords[i[0]] = i[1].count(word)
        return dictWords
    def __cleaning(self, line, *chars):
        chars = list(chars)
        for ch in chars:
            if " " in ch:
                line = line.replace(ch," ")
            else:
                line = line.replace(ch, "")
        return line


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
