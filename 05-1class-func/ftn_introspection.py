# 1. 함수 인수에 대한 정보 추출하기
from clip import clip
clip.__defaults__ # (80,) ; default 셋팅을 확인
clip.__code__ # <code object clip at 0x
clip.__code__.co_varnames # ('text', 'max_len', 'end', 'space_before', 'space_after')
clip.__code__.co_argcount # 2

# 2. inspect 모듈로 깔끔하게 함수 시그니처 추출하기
from clip import clip
from inspect import signature
sig = signature(clip)
str(sig) # '(text, max_len=80)'
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

# 3. inspect 모듈로 함수 시그니처를 인수들의 딕셔너리 바인딩시켜서 argument를 조사해보자.
from tagger import tag
sig = signature(tag)
my_tag = {'name' : 'img', 'title' : 'Sunset Boulevard',
          'src' : 'sunset.jpg', 'cls': 'framed'}
bind_args = sig.bind(**my_tag) # 클래스와 인스턴스의 차이라고 느끼면 될 듯(이게 인스턴스고 위가 클래스)
for name, value in bind_args.arguments.items():
    print(name, '=', value)

# 4. 함수 시그니처에서 애너테이션 추출하기
from clip_annot import clip
sig = signature(clip)
sig.return_annotation # <class 'str'>
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)


# 5. 클래스에서 attribute만 꺼내오기
import inspect

class NewClass(object):
    def __init__(self, number):
        self.multi = int(number) * 2
        self.str = str(number)

    def func_1(self):
        pass

a = NewClass(2)

for i in inspect.getmembers(a):
    # Ignores anything starting with underscore 
    # (that is, private and protected attributes)
    if not i[0].startswith('_'):
        # Ignores methods
        if not inspect.ismethod(i[1]):
            print(i)