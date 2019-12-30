"""Download flags of top 20 countries by population

ThreadPoolExecutor version

Sample run::

    $ python3 flags_threadpool.py
    BD retrieved.
    EG retrieved.
    CN retrieved.
    ...
    PH retrieved.
    US retrieved.
    IR retrieved.
    20 flags downloaded in 0.93s

"""
# BEGIN FLAGS_THREADPOOL
from concurrent import futures # ThreadPoolExecutor와 ProcessPoolExecutor는 콜러블 객체를 서로 다른 스레드나 프로세스에서 실행할 수 있게 해주는 인터페이스 구현

from flags import save_flag, get_flag, show, main  # <1> download_many 빼고 재활용

MAX_WORKERS = 20  # <2> ThreadPoolExecutor에서 사용할 최대 스레드 수


def download_one(cc):  # <3> 하나의 이미지를 내려받을 함수; 각 스레드에서 이 함수 실행 예정
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # <4> 작업자 스레드 수를 설정
    with futures.ThreadPoolExecutor(workers) as executor:  # <5>
        res = executor.map(download_one, sorted(cc_list))  # <6> 작업자 스레드로 download_one 동시 호출; res에 제너레이터 바인딩

    return len(list(res))  # <7> 만약 제너레이터의 스레드로 호출한 함수가 예외를 발생했으면 이터레이블을 list로 바꾸면서(next호출) 발생 


if __name__ == '__main__':
    main(download_many)  # <8>
# END FLAGS_THREADPOOL