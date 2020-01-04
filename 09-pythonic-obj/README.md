# 요약(복습)

`__repr__(self)` : 개발자 문자열 ; return str



 `__str__(self) ` : 사용자 문자열 ; return str



`__iter__(self)` : 이게 구현된 클래스는 iterable 객체를 생성 ; return iterator(generator)



`__format__(self)`



`@classmethod` : 클래스에 묶이는 메소드(첫번째 인자로 self가 아닌 cls를 받는다)



`@staticmethod` : 클래스 또는 객체에 묶이지 않는 함수 ; 연관이 있는 함수라는 걸 나타낼 떄 쓰는데 이걸 쓸 바에 바로 아랫줄에 쓰는 게 나음

`@property` : 객체 attribute를 읽기전용으로 만드는 방법 ; setter를 정의하면 읽고 쓸 수는 있는데 메커니즘이 조금 달라서 19장에서 언급



`self._x` : 보호 attribute

`self.__x` : 비공개 attribute ; 하지만 `obj_name.__dict__`를 입력해보면 접근 가능함을 알 수 있음 ; 건들지 말자



`__slots__`: 클래스 객체는 여기서 명시된 속성만 가질 수 있다. ; 메모지절약(객체마다 dict를 유지할 필요 없음); dict는 hashmapping이라서 메모리를 많이 차지함



클래스 속성 오버라이드 테크닉; `A.class_attr = 'b'`라고 하는 것보다 영구적으로 할거면

```python
class A:
    class_attr = 'f'
    
    def func1(self):
        print(class_attr)
        
class B(A):
    class_attr = 'b'
```



`eval()` : str을 받아서 명령어를 실행