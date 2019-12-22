import collections

# 네임드 튜플이란?
# a = Card(10, 20)
# a.suit
# 코드의 가독성을 위해서 튜플을 대신한다. 하지만 딕셔너리를 사용하지 않는 이유는
# 불변성과 메모리 낭비를 줄이기 위해서이다. 만약에 사전으로 바꾸고 싶다면 a._asdict()
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
beer_card # Card(rank='7', suit='diamonds')


# 카드가 몇장 있는 지, __len__ 이라는 특별 메서드를 호출
deck = FrenchDeck()
len(deck) # 52 


# 인덱스로 카드 읽기, __getitem__ 호출
deck[0] # Card(rank='2', suit='spades')
deck[-1] # Card(rank='A', suit='hearts')
# 이를 활용하여 랜덤하게 하나를 메서드 정의 없이 뽑을 수 있다.
# __getitem__ 이 정의된 객체는 시퀀스([index]로 접근 가능)라고 불리고 슬라이싱도 지원한다.


# PSL의 random.choice()를 활용하면 무작위로 골라낼 수 있다.
from random import choice
choice(deck)


# 정렬
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) # index('item')은 'item'의 위치
    return rank_value * len(suit_values) + suit_values[card.suit]

sorted(deck._cards, key=spades_high)


# 지금까지 구현한 것으로는 카드 셔플링을 할 수 없다. _cards가 불변객체라서 제거가 안됨
# 이를 위해선 __setitem__()을 사용 ; 11장