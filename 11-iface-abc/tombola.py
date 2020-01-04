# BEGIN TOMBOLA_ABC

import abc

class Tombola(abc.ABC):  # <1> ABC를 정의할 땐 abc.ABC를 상속해야한다

    @abc.abstractmethod
    def load(self, iterable):  # <2> 추상메서드는 데코레이트 한 뒤에 docstring만 만들자.
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):  # <3> 추상메서드는 데코레이트 한 뒤에 docstring만 만들자.
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):  # <4> ABC에도 concrete 메서드가 들어갈 수 있다.
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  # <5> 

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  # concrete 서브클래스가 어떻게 저장했을 진 모르지만 빌 때까지 pick을 계속해서 리스트를 뽑아 낼 수 있음
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # <7>
        return tuple(sorted(items))

# END TOMBOLA_ABC

if __name__ == '__main__':
    # ABC가 인터페이스 검사를 제대로 수행하는 지 확인하는 코드
    class Fake(Tombola):
        def pick(self):
            return 13

    f = Fake() # 추상메서드 loaded를 구현하지 않아서 인스턴스화 되지 않음
    
    @Tombola.register
    class Fake2():
        def pick(self):
            return 13

    f = Fake2()
    f.pick()