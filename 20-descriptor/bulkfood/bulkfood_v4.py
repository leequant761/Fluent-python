# BEGIN LINEITEM_V4 : 속성몀을 반복하고 싶지 않다
class Quantity:
    __counter = 0  # <1> Quantity 객체의 수를 샌다 (2개가 될 예정)

    def __init__(self):
        cls = self.__class__  # <2> Quantity 클래스 참조
        prefix = cls.__name__ # 'Quantity'
        index = cls.__counter # 몇번째에 생성됐냐
        self.storage_name = '_{}#{}'.format(prefix, index)  # <3> Quantity
        cls.__counter += 1  # <4>

    def __get__(self, instance, owner):  # <5> 이전엔 객체 초기화에 attr_name이 들어와서 구현할 필요가 없었으나 이젠  찾아줘야한다.
        """
        :param instance: LineItem 객체에 대한 참조
        :param owner: 관리 대상 클래스(LineItem)에 대한 참조 ; print(owner.__name__) 해보샘; 넘어오니깐 그냥 받기만 하는 느낌
        """
        return getattr(instance, self.storage_name)  # <6> 이 함수는 a.weight, a.price 라고 입력할 떄 실행

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)  # <7>
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()  # <8> 이젠 속성명을 전달하지 않아도 된다!
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
# END LINEITEM_V4

if __name__=='__main__':
    coconuts = LineItem('Brazilian coconut', 20, 17.95)
    coconuts.weight, coconuts.price
    getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1') # 디스크립터에서 정의한 속성명으로 접근 가능