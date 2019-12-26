import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):  # <1> 카드를 섞기위해 뮤터블
        self._cards[position] = value

    def __delitem__(self, position):  # <2> MutableSequence를 상속했으니 무조건 추상메서드 구현해야함
        del self._cards[position]

    def insert(self, position, value):  # <3> MutableSequence를 상속했으니 무조건 추상메서드 구현해야함
        self._cards.insert(position, value)
