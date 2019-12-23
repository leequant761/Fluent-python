# 1. 일급객체
def factorial(n):
    '''return n!'''
    return 1 if n < 1 else n * factorial(n-1)
    
factorial(42)
# 속성이 있는 것으로 보아 함수는 function class의 객체이다.
factorial.__doc__ # 'return n!'
type(factorial) # <class 'function'>

# 변수로 참조하기
fact = factorial
fact

# 다른 함수의 인수로 전달하기
list(map(factorial, range(11)))
# >>> [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# 2. 일급함수가 있으면 함수형 스타일로 프로그래밍할 수 있다.
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'rasberry', 'banana']
sorted(fruits, key=len)

def reverse(word):
    return word[::-1]
sorted(fruits, key=reverse)


# 3. map(), filter(), reduce()의 대안 : 리스트,제너레이터컴프리헨션
list(map(fact, range(6))) # [1, 1, 2, 6, 24, 120]
[fact(n) for n in range(6)]# [1, 1, 2, 6, 24, 120]

list(map(fact, filter(lambda n : n % 2, range(6)))) # [1, 6, 120]
[factorial(n) for n in range(6) if n % 2] # [1, 6, 120]

# reduce는 주로 합계를 구학 위해 사용되는데 sum을 사용하는 게 낫다.
from functools import reduce
from operator import add
reduce(add, range(100)) # 4950
sum(range(100))# 4950


# 4. 람다함수
sorted(fruits, key=lambda word: word[::-1])
# 고위함수의 인수 외에는 사용하지 않음; 구문 제한 때문에 복잡해지면 가독성 떨어짐