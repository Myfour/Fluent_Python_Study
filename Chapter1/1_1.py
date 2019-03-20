# python风格的纸牌
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(x, y) for x in self.ranks for y in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    x = FrenchDeck()
    print(x.ranks)
    print(x.suits)
    print(len(x))
    print(x[10])
    print(f'第一张牌{x[0]},最后一张牌{x[-1]}')
    print('随记获取一个集合中的元素random.choice')
    import random
    print(random.choice(x))
    print('最上面3张牌')
    print(x[:3])
    print('所有的A牌')
    print(x[12::13])
    print('实现了__getitem__后变为了可迭代对象')
    for i in x:
        print(i)
    print('----------------------')
    print(len(suit_values))  # 字典的长度为其属性的数量
    print('----------------------')
    for i in sorted(x, key=spades_high):  # 为牌排序，通过key参数设置了排序的规则
        print(i)
