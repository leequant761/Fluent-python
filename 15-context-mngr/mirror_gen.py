"""
A "mirroring" ``stdout`` context manager.

While active, the context manager reverses text output to
``stdout``::

# BEGIN MIRROR_GEN_DEMO_1

    >>> from mirror_gen import looking_glass
    >>> with looking_glass() as what:  # <1>
    ...      print('Alice, Kitty and Snowdrop')
    ...      print(what)
    ...
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'

# END MIRROR_GEN_DEMO_1


This exposes the context manager operation::

# BEGIN MIRROR_GEN_DEMO_2

    >>> from mirror_gen import looking_glass
    >>> manager = looking_glass()  # <1> 
    >>> manager  # doctest: +ELLIPSIS
    <contextlib._GeneratorContextManager object at 0x...>
    >>> monster = manager.__enter__()  # <2>
    >>> monster == 'JABBERWOCKY'  # <3>
    eurT
    >>> monster
    'YKCOWREBBAJ'
    >>> manager  # doctest: +ELLIPSIS
    >...x0 ta tcejbo reganaMtxetnoCrotareneG_.biltxetnoc<
    >>> manager.__exit__(None, None, None)  # <4>
    >>> monster
    'JABBERWOCKY'

# END MIRROR_GEN_DEMO_2

"""


# BEGIN MIRROR_GEN_EX

import contextlib


@contextlib.contextmanager  # <1>
def looking_glass():
    import sys
    original_write = sys.stdout.write  # <2> 함수 클래스 참조(클래스 말고 객체를 참조할 떈 메모리 공유임. 단, 해쉬 가능한 객체 할당은 그렇지 않음)

    def reverse_write(text):  # <3>
        original_write(text[::-1])

    sys.stdout.write = reverse_write  # <4>
    yield 'JABBERWOCKY'  # <5> 여기에서 이 값을 바인딩하고 일시 중단 됨
    sys.stdout.write = original_write  # <6> 원상 복구


# END MIRROR_GEN_EX

if __name__=='__main__':
    with looking_glass() as what:
        print('ABCDEFG') # GFEDCBA; 역순
        print(1/0)
        print(what) # YKCOWREBBAJ; 역순
    print(what) # JABBERWOCKY; 정상