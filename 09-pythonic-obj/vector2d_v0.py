"""
우리가 만들 Vector2d 객체가 수행할 기본적인

    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)  # <1>
    3.0 4.0
    >>> x, y = v1  # <2> 언패킹 가능
    >>> x, y
    (3.0, 4.0)
    >>> v1  # <3> 객체를 생성하는 생성자 소스코드로 출력
    Vector2d(3.0, 4.0)
    >>> v1_clone = eval(repr(v1))  # <4> 생성자코드가 실제로 맞는 지 확인
    >>> v1 == v1_clone  # <5> 두 객체는 서로 같은가?
    True
    >>> print(v1)  # <6>
    (3.0, 4.0)
    >>> octets = bytes(v1)  # <7> 이진표현
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)  # <8>
    5.0
    >>> bool(v1), bool(Vector2d(0, 0))  # <9> origin이냐 아니냐
    (True, False)

"""

# BEGIN VECTOR2D_V0
from array import array
import math


class Vector2d:
    typecode = 'd'  # <1> Vector2d와 bytes 간의 변환에 사용

    def __init__(self, x, y):
        self.x = float(x)    # <2> 숫자를 float객체로 재생성해줘야 조기에 에러 잡힘
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <3> 이터레이블 객체가 됨, 제너레이터로

    def __repr__(self):
        class_name = type(self).__name__ # 'Vector2d'
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4> (x, y)

    def __str__(self):
        return str(tuple(self))  # <5>

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # <6>
                bytes(array(self.typecode, self)))  # <7>

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # <8>

    def __abs__(self):
        return math.hypot(self.x, self.y)  # <9>

    def __bool__(self):
        return bool(abs(self))  # <10>
# END VECTOR2D_V0
