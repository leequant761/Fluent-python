"""StrKeyDict always converts non-string keys to `str`

Test for initializer: keys are converted to `str`.

    >>> d = StrKeyDict([(2, 'two'), ('4', 'four')])
    >>> sorted(d.keys())
    ['2', '4']

Tests for item retrieval using `d[key]` notation::

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

Test for item assignment using non-string key::

    >>> d[0] = 'zero'
    >>> d['0']
    'zero'

Tests for update using a `dict` or a sequence of pairs::

    >>> d.update({6:'six', '8':'eight'})
    >>> sorted(d.keys())
    ['0', '2', '4', '6', '8']
    >>> d.update([(10, 'ten'), ('12', 'twelve')])
    >>> sorted(d.keys())
    ['0', '10', '12', '2', '4', '6', '8']
    >>> d.update([1, 3, 5])
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not iterable

"""
# BEGIN STRKEYDICT

import collections

# 내장클래스를 상속할 때 발생하는 문제 때문에 UserDict가 편하다.(12장 1절)
class StrKeyDict(collections.UserDict):  # <1> collections.UserDict 상속

    def __missing__(self, key):  # <2>
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # <3> 이번엔 .keys() 없이 바로 조회가능

    def __setitem__(self, key, item):
        self.data[str(key)] = item   # <4> 재귀호출 걱정 없고 간단하게 str 형으로 저장

# END STRKEYDICT
