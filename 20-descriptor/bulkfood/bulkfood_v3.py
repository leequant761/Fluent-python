# BEGIN LINEITEM_V3
class Quantity:  # <1> 디스크립터 프로토콜

    def __init__(self, storage_name):
        self.storage_name = storage_name  # <2> 관리 대상 객체(LineItem)에서 값을 보관할 곳

    def __set__(self, instance, value):  # <3> instance에는 LineItem 객체가 들어갈 것이고 value는 할당 값이 들어간다
        if value > 0:
            instance.__dict__[self.storage_name] = value  # <4> 값 할당
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')  # <5> 디스크립터 객체는 딱 2개만 있다.
    price = Quantity('price')  # <6> 하지만 이런 이름반복 코딩스타일은 좋지 못하다. attribute 이름에 의존하기 떄문에; 21장 메타클래스

    def __init__(self, description, weight, price):  # <7>
        self.description = description
        self.weight = weight # self.weight은 각 Lineitem 객체마다 있으니 수천개가 있을 수 있음
        self.price = price

    def subtotal(self):
        return self.weight * self.price
# END LINEITEM_V3

if __name__=='__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    raisins.weight, raisins.description, raisins.price # (10, 'Golden raisins', 6.95)
    raisins.subtotal() # 69.5
    # raisins.weight = -20 # value must be > 0
    raisins.weight # 10

    # 보호된 attribute에 접근 가능; descriptor가 가리기는 한데 접근은 가능함 (__dict__ 도 가능)
    raisins.__dict__['weight']
    raisins.__dict__['weight'] = -100
    raisins.weight # -100