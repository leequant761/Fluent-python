# BEGIN EXPLORE0
from collections import abc


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)  # <1> mapping 인수로 부터 딕셔너리 생성

    def __getattr__(self, name):  # <2> name 속성(attribute)이 없을 떄 호출되며
        if hasattr(self.__data, name):
            return getattr(self.__data, name)  # <3> __data가 name이라는 속성을 갖고있다면 그 속성 반환
        else:
            return FrozenJSON.build(self.__data[name])  # <4> 그렇지 않으면 name을 키로 build를 실행하고 결과를 반환

    @classmethod
    def build(cls, obj):  # <5>
        if isinstance(obj, abc.Mapping):  # <6> __data[name] 즉, 내포된 자료형이 매핑형이면 
            return cls(obj) # 그걸로 FrozenJSON을 만들어서 반환
        elif isinstance(obj, abc.MutableSequence):  # <7> 내포된 자료형이 리스트면
            return [cls.build(item) for item in obj] # 각 아이템이 딕셔너리면 FrozenJSON 리스트면 또 리스트 그냥 숫자면 그대로 반환
        else:  # <8> 리스트 딕셔너리 아니면 그냥 반환
            return obj
# END EXPLORE0

if __name__=='__main__':
    from osconfeed import load
    raw_feed = load()
    feed = FrozenJSON(raw_feed)  # <1> 내포된 딕셔너리와 리스트로 구성된 raw_feed로부터 FrozenJSON 객체 생성
    len(feed.Schedule.speakers)  # <2> . 표기법을 통해서 순회할 수 있다.

    sorted(feed.Schedule.keys())  # <3> 레코드 컬렉션 명을 가져올 수 있다.

    for key, value in sorted(feed.Schedule.items()): # <4> 컬렉션 명과 내용물을 가져올 수 있다.
        print('{:3} {}'.format(len(value), key))

    feed.Schedule.speakers[-1].name  # <5> get_attr과 build함수를 통해 마지막 스피커의 이름

    talk = feed.Schedule.events[40]
    type(talk)  # <6> 제이슨에서 딕셔너리는 프로즌제이슨으로

    talk.name

    talk.speakers  # <7> 스피커 ID

    talk.flavor  # <8> 없는 attribute를 읽으려고 하면 KeyError 발생