# clockdeco.py
# functools.wraps 데코레이터를 사용하면 속성과 키워드 가변인수 문제 해결

import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs): # 함수에서 사용하는 임의의 개수의 위치 argument를 받는다
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

# clockdeco_demo2.py