# clockdeco.py

import time


def clock(func):
    def clocked(*args): # 함수에서 사용하는 임의의 개수의 위치 argument를 받는다
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

# clockdeco_demo.py