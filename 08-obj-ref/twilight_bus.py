# BEGIN TWILIGHT_BUS_CLASS
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            self.passengers = passengers  #<2> 가변형 매개변수는 참조하지말고
            # self.passengers = list(passengers) # 복사를 하자 + 다형성(튜플..)지원

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# END TWILIGHT_BUS_CLASS

# 함수에 가변매개변수를 방어적으로 처리하자.
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
basketball_team # ['Sue', 'Maya', 'Diana'] ; 버스 하차를 하면  팀원이 사라지게 된다!

