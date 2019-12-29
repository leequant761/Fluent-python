"""
Coroutine closing demonstration::

# BEGIN DEMO_CORO_EXC_1
    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.send(22)
    -> coroutine received: 22
    >>> exc_coro.close()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'

# END DEMO_CORO_EXC_1

Coroutine handling exception::

# BEGIN DEMO_CORO_EXC_2
    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(DemoException)
    *** DemoException handled. Continuing...
    >>> getgeneratorstate(exc_coro)
    'GEN_SUSPENDED'

# END DEMO_CORO_EXC_2

Coroutine not handling exception::

# BEGIN DEMO_CORO_EXC_3
    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(ZeroDivisionError)
    Traceback (most recent call last):
      ...
    ZeroDivisionError
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'

# END DEMO_CORO_EXC_3
"""

# BEGIN EX_CORO_EXC
class DemoException(Exception):
    """An exception type for the demonstration."""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:  # <1>
            print('*** DemoException handled. Continuing...')
        else:  # <2>
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')  # <3> 무한루프는 처리되지 않은 예외로만 탈출 가능한데, 그 경우 코루틴 실행이 중단되기 떄문에 실행 안됨
# END EX_CORO_EXC

if __name__=='__main__':
    exc_coro = demo_exc_handling()
    next(exc_coro) # -> coroutine started
    exc_coro.send(11) # -> coroutine received: 11
    exc_coro.send(22) # -> coroutine received: 22
    exc_coro.close() 
    from inspect import getgeneratorstate
    getgeneratorstate(exc_coro) # GEN_CLOSED

    exc_coro = demo_exc_handling()
    next(exc_coro) # -> coroutine started
    exc_coro.send(11) # -> coroutine received: 11
    exc_coro.throw(DemoException) # *** DemoException handled. Continuing...
    getgeneratorstate(exc_coro) # GEN_SUSPENDED
    exc_coro.throw(ZeroDivisionError) # 
    getgeneratorstate(exc_coro) # GEN_CLOSED; 처리할 수 없는 예외를 던져주면 코루틴이 종료된다.
    