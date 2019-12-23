import bisect
import random

# insort : 정렬은 값비싼 연산이므로 정렬한 훙는 정렬 상태를 유지하는 것이 좋음.
# 특히, insort는 정렬된 배열을 유지하면서 지속적으로 항목을 추가할 떄 쓰인다.
# 인수로 들어온 my_list의 사본을 만들지 않고 객체를 직접 변경한다.
# lo, hi를 설정해서 검색 범위를 설정할 수도 있다.
SIZE = 7

random.seed(1729)

my_list = [] # 숫자로 된 리스트를 다루고 있다면 array, queue, deque 쓰는 것이 좋다. See 2.9
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item) # 지속적으로
    print('%2d ->' % new_item, my_list)