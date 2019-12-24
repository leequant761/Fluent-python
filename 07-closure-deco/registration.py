# BEGIN REGISTRATION

registry = []  # <1>

def register(func):  # <2>
    print('running register(%s)' % func)  # <3>
    registry.append(func)  # <4> 함수를 레지스트리에 추가
    return func  # <5> 데코레이터는 함수(콜러블)를 반환

@register  # <6>
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():  # <7>
    print('running f3()')

def main():  # <8>
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()  # <9> 

# END REGISTRATION