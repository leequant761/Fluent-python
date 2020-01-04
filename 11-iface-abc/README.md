프로토콜 : 어떤 역할을 완수하기 위한 메서드 집합; 인터페이스지만 비공식적이다 (ABC처럼 강제로 메서드 구현시키진 않음)

X와 같은 객체, X 프로토콜, X 인터페이스는 다 같은 말이다.

Sequence ABC UML 다이어그램을 보면 구현해야하는게 많은데 파이썬에서 `__getitem__(self, index)`만 구현해도 알아서 시퀀스 프로토콜이 된다.

멍키패칭(monkey patch) : 클래스나 모듈 내부에 정의된 것을 코드를 바꾸지 않고 변경하는 행위

덕타이핑 : 프로토콜을 구현하는 한 자료형에 상관없이 객체를 작동시키는 코드 (내부에 type, isinstance를 안씀)

## 구스타이핑

구스타이핑 : isinstance(obj, cls)를 써도 됨

numbers, collections.abc에 있는 ABC를 여러분이 구현할 때 항상 ABC를 상속하거나 register하라.

isinstance를 검사하는 것은 "이봐, 나를 호출하려면 자네는 이걸 구현해야 해"라고 말하는 것이다.

ABC를 상속하는 것은 개발자의 의도를 명확히 나타낸다.

instance가 다른 경우(다형성을 지원하는 경우) 안에 if문을 통해 디스패치 논리를 구현하기 보다는 인터프리터가 적절한 메서드를 호출할 수 있게 구현

```python
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
```

참고로 데코레이터를 쌓을 때 `@abstractmethod`를 가장 안쪽에 위치시켜야한다.

`@ABC.register` : 가상서브클래스로 등록 (실제로 상속하지는 않음) ;

```python
@Tombola.register
class Fake2():
    def pick(self):
        return 13

f = Fake2()
f.pick()
```

