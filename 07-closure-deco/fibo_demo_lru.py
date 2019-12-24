import functools

from clockdeco import clock

@functools.lru_cache() # <1> argument(optional) 받기 때문에 일반 함수처럼 데코
@clock  # <2>
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))

# functools.lru_cache(maxsize=128, typed=False)
# maxsize : 얼마나 많은 호출을 저장할 지, 꽉 차면 오래된 것 먼저 버림, 2의 제곱으로
# typed : 인수의 자료형이 다르면 다르게 저장; 1 과 1.0