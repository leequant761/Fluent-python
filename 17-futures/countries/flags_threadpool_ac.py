"""Download flags of top 20 countries by population

ThreadPoolExecutor version 2, with ``as_completed``.

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
from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


# executor.map()을 submit()과 as_completed()로 풀어 쓴 것(17줄)
def download_many(cc_list):
    cc_list = cc_list[:5]  # <1> 다섯개의 국가에대해서만
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  # <2> 대기중인 Future 객체를 출력하려고 3개로 제한
        to_do = []
        for cc in sorted(cc_list):  # <3>
            future = executor.submit(download_one, cc)  # <4> 콜러블(download_one)이 실행되도록 스케쥴링; future에는 Future 객체 반환
            to_do.append(future)  # <5>
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))  # <6>

        results = []
        for future in futures.as_completed(to_do):  # <7> Future가 완료될 때 해당 Future를 생성; 즉 포문인데 기다리고있는 포문
            res = future.result()  # <8> Future 객체의 결과를 가져옴
            msg = '{} result: {!r}'
            print(msg.format(future, res)) # <9>
            results.append(res)

    return len(results)
# END FLAGS_THREADPOOL_AS_COMPLETED

if __name__ == '__main__':
    main(download_many)