"""
A coroutine to compute a running average.

Testing ``averager`` by itself::

    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)
    >>> coro_avg.send(None)
    Traceback (most recent call last):
       ...
    StopIteration: Result(count=3, average=15.5)


Driving it with ``yield from``::

    >>> def summarize(results):
    ...     while True:
    ...         result = yield from averager()
    ...         results.append(result)
    ...
    >>> results = []
    >>> summary = summarize(results)
    >>> next(summary)
    >>> for height in data['girls;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> for height in data['boys;m']:
    ...     summary.send(height)
    ...
    >>> summary.send(None)
    >>> results == [
    ...     Result(count=10, average=1.4279999999999997),
    ...     Result(count=9, average=1.3888888888888888)
    ... ]
    True

"""

# BEGIN YIELD_FROM_AVERAGER
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # <1> 이전에 작성했던 코루틴인데 여기선 서브제너레이터
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # <4> 이 Result는 yield from averager()의 값이 될 예정, 호출자가 None을 보내줘서 하위 제너레이터에서 리턴문 실행시 dele gen의 이 코루틴을 호출한 곳에서 StopIteration 예외 발생시킴


# the delegating generator
def grouper(results, key):  # <5>
    while True:  # <6>
        results[key] = yield from averager()  # <7> results[key]에 한 averager 코루틴이 바인딩되고 값을 send로 보내면 받을 수 있다.


# the client code, a.k.a. the caller
def main(data):  # <8>
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # <9>
        next(group)  # <10> 코루틴 실행
        for value in values:
            group.send(value)  # <11>
        group.send(None)  # important! <12> 논을 받으면 Result 받음 

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
              result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


if __name__ == '__main__':
    main(data)

# END YIELD_FROM_AVERAGER
