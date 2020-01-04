# 요약(복습)

객체지향 언어에서 변수는 상자가 아님



객체ID는 객체가 소멸될 때 까지 결코 변하지 않음



Identity검사는 `is()`로 한다.



파이썬은 함수에 매개변수를 call by sharing으로 전달한다. (주소를 넘겨준다 생각하면 편함;)

```python
def func1(a):
    a.append(1)
    
input = []
func1(input)
input # [1]
```



가변형을 매개변수 defualt로 사용하지 말자. (주로 `None`을 사용한다.)



가변형을 매개변수로 받으면 `None`인지 확인을 하고 사본을 만들자.

```python
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] # 좋은 관행
        else:
            self.passengers = list(passengers) # 얕은 복사

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
```



del` 명령는 객체를 제거하는 게 아니라 이름을 제거하는 것이다. 가비지 컬렉트는 참조 카운트가 0이 되어야함



약한 참조는 참조 카운트를 증가시키지 않고 객체를 참조한다. 캐시 어블리케이션에서 유용하게 사용

예를 들어 자신의 객체를 모두 알고 있는 클래스를 만들어보자.

```python
import weakref

class A:
    checker = weakref.WeakValueDictionary()

    def __init__(self, x):
        self.x = x
        self.checker[self.__class__] = self

a = A(10)
len(A.checker) # 1
[key for key in A.checker.keys()] # [__main__.A]
del a
len(A.checker) # 0
```