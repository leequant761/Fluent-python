"""
Experiment with ``ThreadPoolExecutor.map``
"""
# BEGIN EXECUTOR_MAP
from time import sleep, strftime
from concurrent import futures


def display(*args):  # <1> 받은 인수에 시간을 찍어준다.
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):  # <2> 메시지 출력한 다음에 n초 동안 잠을 자고 다시 출력한다. 
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10  # <3>


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # <4> Thread 3개를 가진 ThreadPoolExecutor 객체를 생성
    results = executor.map(loiter, range(5))  # <5> loiter(0), loiter(1), loiter(2)가 먼저 실행된다
    display('results:', results)  # <6> executor.map()이 반환한 값을 바로 출력; 일단은 그냥 쌩 제너레이터반환 (0, 10, 20); next호출을 안했으니깐
    display('Waiting for individual results:')
    for i, result in enumerate(results):  # <7>  제너레이터를 계속 next로 출력; 큐에서 하나가 빠지면(next 실행) 그다음 콜러블이 실행
        display('result {}: {}'.format(i, result))


main()
# END EXECUTOR_MAP
# 결과가 0초 1초 1초 2초에 나오는 것으로 보아 스레드는 동시에 실행됨을 알 수 있음; 만약 따로 실행됐으면 10초 걸림

