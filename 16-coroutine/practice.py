def simple_coroutine():
    print('-> coroutine started')
    x1 = yield
    print('-> coroutine received:', x1)
    x2 = yield
    print('-> coroutine received:', x2)

from inspect import getgeneratorstate
my_coro = simple_coroutine()
getgeneratorstate(my_coro) # GEN_CREATED
next(my_coro)
getgeneratorstate(my_coro) # GEN_SUSPENDED
my_coro.send(10)
getgeneratorstate(my_coro) # GEN_SUSPENDED
my_coro.send(20)
getgeneratorstate(my_coro) # GEN_CLOSED

# 코루틴 예외처리
from coroaverager1 import averager
coro_avg = averager()
coro_avg.send(40)
coro_avg.send(50)
coro_avg.send('spam')
coro_avg.send(60) # raise StopIteration
