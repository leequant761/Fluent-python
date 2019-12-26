# BEGIN TOMBOLA_BINGO

import random

from tombola import Tombola

# load() pick() 추상메서드 구현
# loaded()는 상속
# inspect()는 오버라이드
# _call()__은 추가 구현

class BingoCage(Tombola):  # <1>

    def __init__(self, items):
        self._randomizer = random.SystemRandom()  # <2>
        self._items = []
        self.load(items)  # <3> 초기화작업을 load()에게 위임

    def load(self, items):
        self._items.extend(items) # 리스트(iterable)를 extend하면 각 원소가 append됨
        self._randomizer.shuffle(self._items)  # <4>

    def pick(self):  # <5>
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage') # ABC(톰볼라 인터페이스) 따라서

    def inspect(self): # 오버라이드
        return tuple(sorted(self._items))

    def __call__(self):  # <7> Tombola 인터페이스를 만족하는데 필요는 없지만...
        self.pick()

# END TOMBOLA_BINGO

if __name__=='__main__':
    test = BingoCage([1, 2, 3])
    test.load([4, 5, 6])
    test.inspect() # [1, 5, 2, 6, 3, 4]
    test.pick() # 4
    test.inspect() # [1, 5, 2, 6, 3]