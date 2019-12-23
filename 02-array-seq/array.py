# 1. 커다란 실수 배열의 생성 저장 로딩
from array import array
from random import random

floats = array('d', (random() for i in range(10**7))) # 실수 타입의 배열
floats[-1]

# binary 파일에 배열을 저장; array.tofile()
fp = open('floats.bin', 'wb') # write and binary
floats.tofile(fp)
fp.close()

# binary 파일에서 배열을 로딩; array.fromfile()
floats2 = array('d')
fp = open('floats.bin', 'rb') # read and binary
floats2.fromfile(fp, 10**7)
fp.close()

floats2[-1]
floats2 == floats # True
# 이진 파일에서 읽어오면 텍스트 파일에서 파싱하면서 읽는 것 보다 60배, 저장도 7배 빠르다.
# 하지만 객체를 직렬화하는 pickle 모듈이 더 일반적으로 쓰인다.


# 2. 메모리뷰 (뭔 지 모르겠음)
# 메모리뷰는 데이터구조체를 복사하지 않고 메모리를 공유할 수 있게 하는 기법
# 데이터셋이 클 때 아주 중요한 기법
# memoryview.cast() : 또 다른 memoryview 객체를 반환; 동일한 메모리 공유
import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # signed short
memv = memoryview(numbers) # 주어진 객체(numbers)를 참조하는 memoryview 객체
len(memv) # 5
memv[0] # -2

memv_oct = memv.cast('B') # Unsigned char로 형변환
memv_oct.tolist() # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 5
numbers # array('h', [-2, -1, 1024, 1, 2]); 

# 4. 덱 및 기타 큐
# 리스트의 append와 pop(0)로 스택이나 큐를 구현할 수 있지만 0번 인덱스에 삽입은 부담이 크다.
# 덱의 경우에는 양방향에서 처리하는 부담이 똑같다. 대신 중간항목 제거연산에는 비효율적이다.
from collections import deque
dq = deque(range(10), maxlen=10)
dq # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.rotate(3) # rotate : 한쪽에 있는 n개의 항목을 반대쪽으로
dq # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
dq.rotate(-4)
dq # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
dq.appendleft(-1)
dq # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.extend([11, 22, 33]) # 리스트로 한번에 여러개 넣고 싶을 떄
dq # deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33])
dq.extendleft([10, 20, 30, 40]) # extend : 리스트로 한번에 여러개 넣고 싶을 떄
dq # deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8])
