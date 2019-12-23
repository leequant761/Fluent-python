# BEGIN BISECT_DEMO
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30] # 정렬된 시퀀스에
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31] # 정렬을 유지한 채 니들 추가하고 싶다.

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1> 삽입 위치를 찾기
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>

if __name__ == '__main__':

    if sys.argv[-1] == 'left':    # <4> 만약 명령행 인수에 left를 넣고 실행하면
        bisect_fn = bisect.bisect_left # tie가 발생했을 때 왼쪽에 삽임
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5> 선택된 함수명
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    # 예시 : 시험 점수를 입력받아 등급문자를 반환하는 grade함수
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]
    
    print([grade(score) for score in [33, 99, 77, 89, 90, 100]])

# bisect는 정렬된 긴 숫자 시퀀스를 검색할 때 index보다 더 빠르다.
# lo, hi를 설정해서 검색 범위를 설정할 수도 있다.