# clockdeco_demo.py

import time
from clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('8! =', factorial(8))
# 이 방식의 단점은 데커레이트 된 함수의 __name__과 __doc__ 속성을 가린다.
factorial.__name__ # clocked
# 이 문제 해결을 위해 새 데코레이터 모듈 clockdeco2.py 을 보자.