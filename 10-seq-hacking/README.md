# 요약(정리)

프로토콜 : 특정 역할을 수행하기 위한 메서드, 프로퍼티등의 인터페이스를 의미한다. 예를 들어 시퀀스 프로토콜은 `__len__(self)` 과 `__getitem__(self, index)`을 요구한다.



`__getattr__(self, name)` : 없는 속성을 참조할 때 실행되는 함수; return을 안할 경우 `raise AttributeError`를 하자

`__setattr__(self, name)` : 없는 속성을 저장할 때 실행되는 함수; `super().__setattr__(name, value)`을 안할 경우 `raise AttributeError`를 하자



`funcional.reduce(fn, iterable)` : `fn(fn(fn(l[0], l[1]), l[2]), l[3])` ; 

`map(fn, iterable)` : 각 원소에 fn을 적용한 제너레이터 반환



`zip(*iterable, fillvalue=0)` : 이터레이블의 각 원소를 순서별로 튜플로 묶은 제너레이터 반환