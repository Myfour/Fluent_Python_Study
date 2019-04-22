import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


if __name__ == '__main__':
    s = Sentence('"The time has come,"the Walrus said,')
    print('--' * 30)
    print(s)
    print('--' * 30)
    for word in s:
        print(word)
    print('--' * 30)
    print(s[3])
    print('--' * 30)
