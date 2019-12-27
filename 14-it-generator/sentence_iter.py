"""
Sentence: iterate over words using the Iterator Pattern, take #1

WARNING: the Iterator Pattern is much simpler in idiomatic Python;
see: sentence_gen*.py.
"""

# BEGIN SENTENCE_ITER
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence: # iterable object

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # <1>iterable object 프로토콜
        return SentenceIterator(self.words)  # <2> iterable 객체 반환

# iterable object와 iterator를 나눠서 작성한 이유는 디자인 패턴에 맞지 않기 떄문
# 이터레이터는 직접 데이터를 입력시키지 않음

class SentenceIterator: # iterator : iterable 객체 생성자

    def __init__(self, words):
        self.words = words  # <3>
        self.index = 0  # <4>

    def __next__(self): # iterator 프로토콜
        try:
            word = self.words[self.index]  # <5>
        except IndexError:
            raise StopIteration()  # <6> 
        self.index += 1  # <7>
        return word  # <8>

    def __iter__(self):  # <9>iterator 프로토콜 ; 사실 쓸 일은 없음
        return self
# END SENTENCE_ITER

def main():
    import sys
    import warnings
    try:
        filename = sys.argv[1]
        word_number = int(sys.argv[2])
    except (IndexError, ValueError):
        print('Usage: %s <file-name> <word-number>' % sys.argv[0])
        sys.exit(1)
    with open(filename, 'rt', encoding='utf-8') as text_file:
        s = Sentence(text_file.read())
    for n, word in enumerate(s, 1):
        if n == word_number:
            print(word)
            break
    else:
        warnings.warn('last word is #%d, "%s"' % (n, word))

if __name__ == '__main__':
    main()
