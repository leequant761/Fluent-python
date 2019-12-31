# BEGIN SCHEDULE1 딕셔너리 순회하는 것을 생각하면 된다
import warnings

import osconfeed  # <1>

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # <2> 키워드 인수 들어오면 업데이트(attribute로 저장하며) ; 참고로 객체의 attribute는 __dict__에 들어가기 때문에 꼼수로(키워드 argument 넘겨주면) 한번에 정의가능


def load_db(db): # 데이터베이스가 없을 떄 실행되는데
    raw_data = osconfeed.load()  # <3> json파일을 불러와서
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():  # <4> 스케쥴의 아이템들(리스트인데 원소는 딕셔너리임)별로
        record_type = collection[:-1]  # <5> s제거
        for record in rec_list: # record는 딕셔너리임; rec_list는 딕셔너리들의 리스트임
            key = '{}.{}'.format(record_type, record['serial'])  # <6> conference.id, event.id, speaker.id, venue.id
            record['serial'] = key  # <7> 키 변경
            db[key] = Record(**record)  # <8> 변경한 키에 아이템은 키만 살짝바꾼 키워드매개변수로 전달

# END SCHEDULE1

if __name__=='__main__':
    import shelve
    db = shelve.open(DB_NAME)  # <1> 기존 데이터베이스 파일을 열거나 새로 만든다; shelv.Shelf는 새로운 값이 키에 할당될 때마다 키오 값이 저장됨
    if CONFERENCE not in db:  # <2> 데이터 베이스에 데이터가 있는지 확인 ; C
        load_db(db)  # <3> 없다면 데이터베이스를 로딩하자 ; 함수를 통햐 db 객체에는 키와 값이 계속 저장됨

    speaker = db['speaker.3471']  # <4> 스피커 레코드를 가져오자
    type(speaker)  # <5> Record 객체
    speaker.name, speaker.twitter  # <6> ('Anna Martelli Ravenscroft', 'annaraven')
    db.close()  # <7> shelv.Shelf는 사용후에 꼭 닫아줘야한다. ; 가능하면 with문을 사용