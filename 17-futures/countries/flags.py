"""Download flags of top 20 countries by population

Sequential version

Sample run::

    $ python3 flags.py
    BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
    20 flags downloaded in 10.16s

"""
# BEGIN FLAGS_PY
import os
import time
import sys

import requests  # <1> 이는 PSL이 아니므로 한칸 띄워서 임포트

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2> TOP 20 인구 국가

BASE_URL = 'http://flupy.org/data/flags'  # <3> 국기 이미지 웹사이트

DEST_DIR = 'D:/imsi/'  # <4> 이미지 저장 디렉토리


def save_flag(img, filename):  # <5> 
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # <6> 국가 코드를 인수로 받고
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower()) # URL을 만들어서
    resp = requests.get(url) # 응답으로 받은 binarysequence를 
    return resp.content # 반환


def show(text):  # <7> 
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):  # <8> 동시성에서는 달라질 예정
    for cc in sorted(cc_list):  # <9>
        image = get_flag(cc) # 이미지 이진시퀀스
        show(cc) # 나라명 출력
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main(download_many):  # <10> 다운로드하는데 걸린시간 출력
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)  # <11>
# END FLAGS_PY
