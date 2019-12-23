"""StrKeyDict0 converts non-string keys to `str` on lookup

# BEGIN STRKEYDICT0_TESTS

Tests for item retrieval using `d[key]` notation::

    >>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    >>> d['2']
    'two'
    >>> d[4]
    'four'
    >>> d[1]
    Traceback (most recent call last):
      ...
    KeyError: '1'

Tests for item retrieval using `d.get(key)` notation::

    >>> d.get('2')
    'two'
    >>> d.get(4)
    'four'
    >>> d.get(1, 'N/A')
    'N/A'


Tests for the `in` operator::

    >>> 2 in d
    True
    >>> 1 in d
    False

# END STRKEYDICT0_TESTS
"""

# 검색했을 때 키가 존재하지 않는 경우2 ; dict를 상속받고 __missing__ 정의
# BEGIN STRKEYDICT0
class StrKeyDict0(dict):  # <1> dict 상속

    def __missing__(self, key): # 이는 dict의 __getitem__()과 연결되어있음
        if isinstance(key, str):  # <2> 키가 문자열이고 존재하지 않으면 에러발생
            raise KeyError(key)
        return self[str(key)]  # <3> 키가 문자열이 아니면 문자열로 만들고 조회

    def get(self, key, default=None):
        try:
            return self[key]  # <4> 상속받음 dict의 __getitem__()에 위임
        except KeyError:
            return default  # <5> 키 에러가 발생하면 None을 return한다.

    def __contains__(self, key): # __missing__에서 str 구분 없이 했으니
        # 명시적으로 keys(논 파이서닉한)를 넣은 이유는? 무한 재귀 방지
        return key in self.keys() or str(key) in self.keys()  # <6> 명시적으로 key

# END STRKEYDICT0

