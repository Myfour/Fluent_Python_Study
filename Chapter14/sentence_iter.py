import re
import reprlib
RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = Sentence('"The time has come,"the Walrus said,')
    print('--' * 30)
    print(s)
    print('--' * 30)
    for word in s:
        print(word)
    print('--' * 30)
    # print(s[3])
    print('--' * 30)