# BEGIN CORO_DECO
from functools import wraps

def coroutine(func): # 데코레이터는 함수를 받아서 함수를 뱉는다.
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):  # <1> 들어온 함수를 래핑
        gen = func(*args,**kwargs)  # <2> 인자를 넘겨주고
        next(gen)  # <3> 코루틴 실행된 채로
        return gen  # <4> 반환; 즉 next호출 필요 없어짐
    return primer
# END CORO_DECO
