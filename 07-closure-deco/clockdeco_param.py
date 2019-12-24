# clockdeco_param.py

"""
>>> snooze(.1)  # doctest: +ELLIPSIS
[0.101...s] snooze(0.1) -> None
>>> clock('{name}: {elapsed}')(time.sleep)(.2)  # doctest: +ELLIPSIS
sleep: 0.20...
>>> clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
sleep(0.2) dt=0.201s
"""

# BEGIN CLOCKDECO_PARAM (데코레이터 파라미터와 함수자체의 파라미터가 있는 경우)
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):  # <1> 데콜이터 팩토리 (출력 포맷을 결정)
    def decorate(func):      # <2> 데코레이터(래퍼는 아님)
        def clocked(*_args): # <3> 들어오는 함수에 대한 래퍼
            t0 = time.time()
            _result = func(*_args)  # <4>
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # <5> args는 출력문자용
            result = repr(_result)  # <6>
            print(fmt.format(**locals()))  # <7> 현재 스코프에서의 지역변수들을 딕셔너리 형태로 반환
            return _result  # <8>
        return clocked  # <9>
    return decorate  # <10>

if __name__ == '__main__':

    @clock()  # <11>
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

# END CLOCKDECO_PARAM