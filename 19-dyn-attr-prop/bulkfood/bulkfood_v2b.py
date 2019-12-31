# BEGIN LINEITEM_V2B
class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):  # <1> 지극히 평범한 게터
        return self.__weight # __weight이라는 attribute는 정의는 안했지만 property 객체에 이 함수가 들어가면서 위에서 정의한 객체의 attribute를 반환

    def set_weight(self, value):  # <2> 지극히 평범한 세터
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

    weight = property(get_weight, set_weight)  # <3> self.weight에 들어가게 될 weight에 property 컬러블클래스라는 공개 attribute에 할당
    # 그러면 클래스 생성과정을 new init으로 생각해보면 init 함수에서 argument weight에는 이미 정의된 게 들어가는 것임

if __name__=='__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    raisins.weight, raisins.description, raisins.price # (10, 'Golden raisins', 6.95)
    raisins.subtotal() # 69.5
    # raisins.weight = -20 # value must be > 0
    raisins.weight # 10

    # 보호된 attribute에 접근 가능; 클래스 프로퍼티가 가리기는 한데 접근은 가능함 (__dict__ 도 가능)
    raisins._LineItem__weight
    raisins._LineItem__weight = -100
    raisins.weight # -100