"""
Sentence: iterate over words using a generator function
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # <1>
            yield word  # <2> 단어 생성
        return  # <3> 다 소진하고 나면 그냥 나가면 됨

# done! <4> Iterator(next, iter 구현한)를 작성할 필요가 없다.
# 왜냐면 Sentence자체가 iterable한 Generator가 되기 때문이다.

if __name__=='__main__':
# 제너레이터가 어떻게 작동되는 것인 지 보여주는 함수(따로 파일을 내주긴 애매해서 이자리에)
    def gen_AB():
        print('start')
        yield 'A'
        print('continue')
        yield 'B'
        print('end')

    for c in gen_AB():
        print('-->', c)