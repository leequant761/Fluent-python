# 필터링 제너레이터 함수의 예
import itertools

def vowel(c):
    return c.lower() in 'aeiou'

list(filter(vowel, 'Aardvark')) # ['A', 'a', 'a']
list(itertools.filterfalse(vowel, 'Aardvark')) # ['r', 'd', 'v', 'r', 'k']
list(itertools.takewhile(vowel, 'Aardvark')) # ['A', 'a'] ; 거짓이 등장하면 생성안함
list(itertools.dropwhile(vowel, 'Aardvark')) # ['A', 'a'] ; 거짓이 등장하면 생성함
list(itertools.compress('Aardvark', (1, 0, 1, 1, 1, 0, 1))) # ['A', 'r', 'd', 'v', 'r']; 두 반복형을 병렬로 소진될 때 까지 소비, 뒤에것이 참일때 생성함
list(itertools.islice('Aardvark', 4)) # ['A', 'a', 'r', 'd']; s[:4]
list(itertools.islice('Aardvark', 4, 7)) # ['v', 'a', 'r']; s[4:7]
list(itertools.islice('Aardvark', 1, 7, 2)) # ['a', 'd', 'a']; s[1:7:2]

# 매핑 제너레이터 함수
sample = [5, 4, 2,8, 7, 6, 3, 0, 9, 1]
import itertools
list(itertools.accumulate(sample)) # 쌓아가며 생성; sum
list(itertools.accumulate(sample, min)) # 쌓아가며 생성; min
list(itertools.accumulate(sample, max)) # 쌓아가며 생성; max
import operator
list(itertools.accumulate(sample, operator.mul)) # 쌓아가며 생성; multiply

list(enumerate('albatroz', 1))
    # [(1, 'a'),
    # (2, 'l'),
    # (3, 'b'),
    # (4, 'a'),
    # (5, 't'),
    # (6, 'r'),
    # (7, 'o'),
    # (8, 'z')]
list(map(operator.mul, range(11), range(11))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(map(operator.mul, range(11), [2, 4, 8])) # [0, 4, 16]
list(map(lambda a, b: (a, b), range(11), [2, 4, 8])) # [(0, 2), (1, 4), (2, 8)]
list(itertools.starmap(lambda a, b: a*b, enumerate('albatroz', 1)))
    # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']

# 병합 제너레이터 함수의 예 : 여러 iterable을 하나의 제너레이터로
list(itertools.chain('ABC', range(2))) # ['A', 'B', 'C', 0, 1]
list(itertools.chain.from_iterable([[1, 2], [3, 4]])) # [1, 2, 3, 4]
list(zip('ABC', range(5), [10, 20, 30, 40])) # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
list(itertools.zip_longest('ABC', range(5), [10, 20, 30, 40], fillvalue='?'))
    # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30), ('?', 3, 40), ('?', 4, '?')]
list(itertools.product('ABCD', '+0-'))
    # [('A', '+'),
    # ('A', '0'),
    # ('A', '-'),
    # ('B', '+'),
    # ('B', '0'),
    # ('B', '-'),
    # ('C', '+'),
    # ('C', '0'),
    # ('C', '-'),
    # ('D', '+'),
    # ('D', '0'),
    # ('D', '-')]

# 항목 하나를 여러개로 확장하는 제너레이터 함수
ct = itertools.count()
next(ct) # 0
next(ct) # 1
next(ct) # 2
list(itertools.islice(itertools.count(1, .3), 3)) # [1, 1.3, 1.6]; infty_seq[:3]
cy = itertools.cycle('ABC')
list(itertools.islice(cy, 7)) # ['A', 'B', 'C', 'A', 'B', 'C', 'A']
rp = itertools.repeat(7) # 7 무한 수열;
next(rp), next(rp) # (7, 7)
list(itertools.repeat(8, 4)) # [8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5))) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# 순열조합 제너레이터 함수
list(itertools.combinations('ABC', 2))
list(itertools.combinations_with_replacement('ABC', 2))
list(itertools.permutations('ABC', 2))
list(itertools.product('ABC', repeat=2))

# 재배치 제너레이터 함수
list(itertools.groupby('LLLLAAGGG'))
    # [('L', <itertools._grouper at 0x27f6c127208>),
    #  ('A', <itertools._grouper at 0x27f6c1274c8>),
    #  ('G', <itertools._grouper at 0x27f6c127388>)]]
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len) # 미리 필수로 해줘야함
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

list(itertools.tee('ABC')) # 여러 제너레이터 생성 가능 n=2가 default
g1, g2 = itertools.tee('ABC')
list(g1) # ['A', 'B', 'C']
list(g1) # []