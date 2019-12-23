# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# BEGIN INDEX_DEFAULT (존재하지 않는 키에 대한 또 다른 처리)
"""Build an index mapping word -> list of occurrences"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)     # index.default_factory : list
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # 없는 걸 호출하면 새 default_factory를 참조

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX_DEFAULT
