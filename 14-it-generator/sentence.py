"""
Sentence: access words by index
반복형에 대해 알아보자
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # <1> 정규표현식에 매칭되는 문자열 리ㅡ트

    def __getitem__(self, index): # 시퀀스 프로토콜
        return self.words[index]  # <2> 해당하는 인덱스의 단어 반환

    def __len__(self):  # <3> 시퀀스 프로토콜
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4> 너무 길면 축약

if __name__=='__main__':
    s = Sentence('"The time hase come," the Walrus said,')
    print(s)
    
    for word in s: # 시퀀스 프로토콜은 반복할 수 있다. __iter__가 구현이 안되어있으면 __getitem__에 위임
        print(word)
    # 실제로는 다음과 같음
    # it = iter(s)
    # while True:
    #     try:
    #         print(next(it))
    #     except StopIteration:
    #         del it
    #         break
    
    print(list(s))

    # 하지만 구스타이핑기법을 사용하면 iterable하진 않음
    from collections import abc
    print(issubclass(Sentence, abc.Iterable))

