# BEGIN REGISTRATION_PARAM (매개변수를 포함하는 데커레이터)

registry = set()  # <1>

def register(active=True):  # <2> 이제 register(데코레이터 팩토리)는 선택적 인수를 받고
    def decorate(func):  # <3> decorate가 함수를 인수로 받는다.
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:   # <4> active일떄만 등록한다
            registry.add(func)
        else:
            registry.discard(func)  # <5> 아니면 버려라

        return func  # <6>
    return decorate  # <7>

@register(active=False)  # <8> 안담김
def f1():
    print('running f1()')

@register()  # <9>
def f2():
    print('running f2()')

def f3():
    print('running f3()')

# END REGISTRATION_PARAM

# 외부 파일에서 이 모듈을 임포트하면 registry에는 f2밖에 안담긴다.