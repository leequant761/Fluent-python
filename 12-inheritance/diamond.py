class A:
    def ping(self):
        print('Aping:', self)


class B(A):
    def pong(self):
        print('Bpong:', self)


class C(A):
    def pong(self):
        print('CPONG:', self)


class D(B, C):

    def ping(self):
        A.ping(self) # super().ping()과 동일
        print('Dpost-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

D.__mro__ # (__main__.D, __main__.B, __main__.C, __main__.A, object)
d = D()
d.pingpong()
'''
    Aping: <__main__.D object at 0x0000018615B6F448>
    Dpost-ping: <__main__.D object at 0x0000018615B6F448>
    Aping: <__main__.D object at 0x0000018615B6F448>
    Bpong: <__main__.D object at 0x0000018615B6F448>
    Bpong: <__main__.D object at 0x0000018615B6F448>
    CPONG: <__main__.D object at 0x0000018615B6F448>
'''

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

import tkinter
print_mro(tkinter.Text)