from random import randrange

from tombola import Tombola

@Tombola.register  # <1> 가상서브클래스로 등록(실제 부모역할안함)
class TomboList(list):  # <2>

    def pick(self):
        if self:  # <3> list에서 self.__bool__ 을 상속받음
            position = randrange(len(self))
            return self.pop(position)  # <4>
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # <5> load라는 메서드를 extend에 위임

    def loaded(self):
        return bool(self)  # <6>

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)  # <7>

# 대신에 서브클래스로판단해서 issubclass(, Tombola)와 isinstance(, Tombola)를 통과
if __name__=='__main__':
    issubclass(TomboList, Tombola)
    t = TomboList(range(100))
    isinstance(t, Tombola)
    
    TomboList.__mro__ # (__main__.TomboList, list, object) ; Tombo는 상속안받음