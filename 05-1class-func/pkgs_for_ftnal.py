# 1. operator 모듈
from functools import reduce
# 재귀 대신에 숫자 시퀀스를 곱하는 경우 (내장 product가 없음)
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))

# 2. from operator itemgetter(); 시퀀스 항목 참조
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(2)):
    print(city)
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# 3. from operator attrgetter(); 객체의 속성을 추출해낸다.
from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data]
# 현재 metrod_areas 컨테이너에는 네임드 튜플 객체들이 저장되어있다.
from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat') # 객체들의 name과 coord.lat을 추출하고 싶다.
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

# 4. from operator methodcaller(); 객체의 메서드를 호출
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper') # 객체의 upper를 호출하자
upcase(s) # 'THE TIME HAS COME'
hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s) # 'The-time-has-come'

# 5. from functools partial()
# functools 모듈을 higher-order function들을 모아놨다. 예를 들어 reduce
# partial도 굉장히 유용; 일부 argument를 고정시킨 콜러블 생성; API에 유용
from operator import mul
from functools import partial
triple = partial(mul, 3)
triple(7) # 21; mul(3, 7)
[triple(i) for i in range(10)] # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
