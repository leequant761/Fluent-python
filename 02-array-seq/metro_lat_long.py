# 튜플 언패킹하기
temp = [(idx, n) for n, idx in enumerate(list('abcde'))]
result = []
for _, n in temp:
    result.append(n)

# 튜플 언패킹하기
a, b = (10, 20)

# 초과 항목을 잡기 위한 병렬 할당
a, b, *rest = range(5)
rest # [2, 3, 4]

# 내포된 튜플 언패킹하기 - 예시
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

# 네임드 튜플
# 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수; 디버깅할 떄 유용
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates') # 클래스명, 필드명
tokyo = City('Tokyo', 'Jp', 36.933, (35.689722, 139.691667))
tokyo.population
tokyo.coordinates
tokyo[1] # 'Jp'


# 네임드 튜플
# 클래스 속성: _fileds 
City._fields # ('name', 'country', 'population', 'coordinates')
# 클래스메서드: _make(iterable) ; return namedtuple
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# 객체메서드: _asdict() ; return OrderedDict
for key, value in delhi._asdict().items():
    print(key + ':', value)

