"""
A coroutine to compute a running average

# BEGIN CORO_AVERAGER_TEST
    >>> coro_avg = averager()  # <1> 코루틴 생성
    >>> next(coro_avg)  # <2> 코루틴 실행
    >>> coro_avg.send(10)  # <3> 이동평균 생성
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

# END CORO_AVERAGER_TEST

"""

# BEGIN CORO_AVERAGER
def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # <1>
        term = yield average  # <2>
        total += term
        count += 1
        average = total/count
# END CORO_AVERAGER
