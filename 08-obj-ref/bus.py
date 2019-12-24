
"""
>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David']
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David']

"""

# BEGIN BUS_CLASS
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers) # 리스트는 mutable 객체라서 얕은 복사를 하면 똑같은 참조를 하게 된다. 

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# END BUS_CLASS

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus2)
print('bus1 :', id(bus1), '/ bus2 :', id(bus2), '/ bus3 :', id(bus3)) # 컨테이너는 다름
bus1.drop('Bill')
bus2.passengers # 하지만 같은 리스트를 참조하고 있다. 
bus3.passengers # 깊은 복사는 객체 안의 참조까지 복사한다.

# deepcopy()
a = [10, 20]
b = [a, 30] # [[10, 20], 30]
a.append(b) # 순환참조 ; [10, 20, [[...], 30]]

from copy import deepcopy
c = deepcopy(a)
id(a[2][0][2]) == id(c[2][0][2]) # False
id(a[2][0][2][0][2]) == id(c[2][0][2][0][2]) # False
