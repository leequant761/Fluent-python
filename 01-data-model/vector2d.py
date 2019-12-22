from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
        # return 'Vector({0}, {1})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 특수 메서드는 직접 호출하지 않는다(rj).

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2 # Vector(4, 5)

v = Vector(3, 4)








from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 특수 메서드는 직접 호출하지 않는다(almost).

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2 # Vector(4, 5)

v = Vector(3, 4)


# __str__ vs __repr__
# 두 메서드를 동시에 정의한다면 __str__은 사용자에게 더 보기 좋은 식으로 표현
# 만약 하나만 정의해야 한다면 __repr__을 정의하면 된다.
# __repr__은 대화형 인터프리터에서 보여줄 뿐만 아니라 __str__이 없을 때 대체하기 떄문이다.


# 사용자 정의 __bool__
# 조건문에서 __bool__을 정의하지 않았다면 __len__을 호출하고 이마저도 없다면
# 그냥 참값으로 본다.