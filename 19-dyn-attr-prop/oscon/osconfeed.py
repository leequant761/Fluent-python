"""
osconfeed.py: Script to download the OSCON schedule feed

# BEGIN OSCONFEED_DEMO

    >>> feed = load()  # <1> 내포된 dictionary 객체
    >>> sorted(feed['Schedule'].keys())  # <2> 4개의 레코드 컬렉션 나열
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed['Schedule'].items()): # 스케쥴 레코드의 
    ...     print('{:3} {}'.format(len(value), key))  # <3> 레코드 출력
    ...
      1 conferences
    484 events
    357 speakers
     53 venues
    >>> feed['Schedule']['speakers'][-1]['name']  # <4>
    'Carina C. Zona'
    >>> feed['Schedule']['speakers'][-1]['serial']  # <5>
    141590
    >>> feed['Schedule']['events'][40]['name']
    'There *Will* Be Bugs'
    >>> feed['Schedule']['events'][40]['speakers']  # <6>
    [3471, 5199]


# END OSCONFEED_DEMO
"""

# BEGIN OSCONFEED
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON): # 만약 파일이 없다면
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # <1> 경고메시지
        with urlopen(URL) as remote, open(JSON, 'wb') as local:  # <2>
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)  # <3> json 파일을 파싱하고 네이티브 파이썬 객체(dict, list, str, int)로 반환

# END OSCONFEED
