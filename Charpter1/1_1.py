# python风格的纸牌
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(x, y) for x in self.suits for y in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    x = FrenchDeck()
    print(x.ranks)
    print(x.suits)
    print(len(x))
    print(x[10])