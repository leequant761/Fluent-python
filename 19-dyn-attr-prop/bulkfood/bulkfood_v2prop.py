# BEGIN LINEITEM_V2_PROP_FACTORY_FUNCTION
def quantity(storage_name):  # <1> 이 argument가 프로퍼티를 어디에 저장할 지 결정

    def qty_getter(instance):  # <2> instance는 LineItem 객체를 가르킴
        return instance.__dict__[storage_name]  # <3> 그 객체에서 attribute를 직접 가져온다

    def qty_setter(instance, value):  # <4> instance는 LineItem 객체를 가르킴
        if value > 0:
            instance.__dict__[storage_name] = value  # <5> 객체 attribute에 value를 저장
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)  # <6> 사용자정의 프로퍼티 객체를 생성해서 반환
# END LINEITEM_V2_PROP_FACTORY_FUNCTION


# BEGIN LINEITEM_V2_PROP_CLASS
# 프로퍼티 팩토리 : 두개의 세터/게터를 직접 구현하지 않고도 속성이 0이상만 받을 수 있게하는 법
class LineItem:
    weight = quantity('weight')  # <1> 프로퍼티 팩토리로생성한 프로퍼티 객체를 class attribute에 저장
    price = quantity('price')  # <2> 프로퍼티 팩토리로생성한 프로퍼티 객체를 class attribute에 저장

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # <3> 0이나 음이되지않게 보장
        self.price = price

    def subtotal(self):
        return self.weight * self.price  # <4> 객체에 저장된 값 가져오기
# END LINEITEM_V2_PROP_CLASS

if __name__=='__main__':
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    nutmeg.weight, nutmeg.price  # <1>

    sorted(vars(nutmeg).items())  # <2> vars는 안의 attribute조사하는 함수
