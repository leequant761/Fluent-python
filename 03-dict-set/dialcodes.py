# BEGIN DIALCODES
# dial codes of the top 10 most populous countries
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)  # <1> 튜플로 딕셔너리 생성 (인구 순서)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))  # <2> 딕셔너리 생성 (번호 순서)
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  # <3> 딕셔너리 생성 (알파벳 순서)
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3  # <4> True ; 키 같고 값 같으니


# 운이 없으면 해시 테이블에서의 키 순서가 달라질 수도 있다.
# 그렇기 때문에 딕셔너리를 반복하는 동안에 딕셔너리의 내용을 변경하는 것은 비추천
# 검색하면서 항목을 추가 하고 싶을 떈 임시 딕셔너리에 추가 한 다음에 다 끝나면 업데이트하기