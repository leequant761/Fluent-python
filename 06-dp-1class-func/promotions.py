from classic_strategy import Customer, LineItem, Order
# Promotion 추상클래스를 제거하고 간단하게 함수로 작성해보자.

class Order(Order):

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self) # promotion이 클래스에서 함수로 들어감
        return self.total() - discount

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

joe = Customer('John Doe', 0)  
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),  
               LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo))  

long_order = [LineItem(str(item_code), 1, 1.0) 
              for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))
