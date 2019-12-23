"""
# BEGIN BINGO_DEMO

>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True

# END BINGO_DEMO

"""

# BEGIN BINGO

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    # __call__() 인스턴스 메서드만 구현하면 객체가 함수처럼 동작한다.
    def __call__(self):  # <5> bingo.pick() 과 bingo()는 같은 역할
        return self.pick()

bingo = BingoCage(range(3))
bingo.pick()
bingo()
callable(bingo) # True

