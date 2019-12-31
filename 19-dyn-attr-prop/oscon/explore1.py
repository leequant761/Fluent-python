from collections import abc
import keyword


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

# BEGIN EXPLORE1
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # <1> 그러므로 파이썬의 키워드 일 경우 앞에 _를 붙이자.
                key += '_'
            self.__data[key] = value
# END EXPLORE1

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:  # <8>
            return obj

if __name__=='__main__':
    grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    grad.name
    # grad.class # 예약어이므로 class 속성을 읽을 수 없다.
    # getattr(grad, 'class_') # 그래서 이렇게 읽어야만 한다.
    grad.class_ # 1982
