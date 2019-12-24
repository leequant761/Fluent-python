# BEGIN HAUNTED_BUS_CLASS
class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):  # <1>mutable
        self.passengers = passengers  # <2>mutable

    def pick(self, name):
        self.passengers.append(name)  # <3>mutable한 객체 변경

    def drop(self, name):
        self.passengers.remove(name)
# END HAUNTED_BUS_CLASS

# 매개변수에 가변형을 넣으면 일어나는일.
bus1 = HauntedBus(['Alice', 'Bill'])
bus1.passengers #['Alice', 'Bill']
bus1.pick('Charlie')
bus1.drop('Alice')
bus1.passengers #['Bill', 'Charlie']
bus2 = HauntedBus()
bus2.pick('Carrie')
bus2.passengers #['Carrie']
bus3 = HauntedBus()
bus3.passengers #['Carrie']
bus3.pick('Dave')
bus2.passengers #['Carrie', 'Dave']
bus2.passengers is bus3.passengers #True
bus1.passengers #['Bill', 'Charlie']

dir(HauntedBus.__init__)  # 클래스를 정의하게 되면 __defaults__라는 속성의 첫번째 항목에 []가 바인딩됨
HauntedBus.__init__.__defaults__ # (['Carrie', 'Dave'],)
HauntedBus.__init__.__defaults__[0] is bus2.passengers # True

# 이런 일 때문에 가변값을 받는 매개변수는 None을 default로 사용하고 
# None을 확인하고 난 뒤에 할당한다.
