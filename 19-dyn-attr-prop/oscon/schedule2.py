# BEGIN SCHEDULE2_RECORD : 목표 events 레코드에서 venue와 speaker레코드를 뺴오자
import warnings
import inspect  # <1>

import osconfeed

DB_NAME = 'data/schedule2_db'  # <2>
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):  # <3>
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented
# END SCHEDULE2_RECORD


# BEGIN SCHEDULE2_DBRECORD
class MissingDatabaseError(RuntimeError):
    """Raised when a database is required but was not set."""  # <1> pass보단 예외 상황을 설명하는게 좋음


class DbRecord(Record):  # <2> Record 상속

    __db = None  # <3> 데이터베이스 참조 보관

    @staticmethod  # <4> 정적메서드;
    def set_db(db):
        DbRecord.__db = db  # <5> class attribute에 db 참조 설정

    @staticmethod  # <6>
    def get_db():
        return DbRecord.__db

    @classmethod  # <7> 클래스 메서드이므로 서브클래스에서 쉽게 커스터마이즈 가능
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]  # <8> 데이터베이스에서 id 레코드 가져오자
        except TypeError:
            if db is None:  # <9> db가 없는 상황이면
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:  # <10> 나머지 예외는 모르니 일단 발생
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):  # <11> 레코드에
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()  # <12>
# END SCHEDULE2_DBRECORD


# BEGIN SCHEDULE2_EVENT
class Event(DbRecord):  # <1> 

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)  # <2> 베뉴의 id로 키를 생성해서 fetch 클래스메서드에 전달

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):  # <3>
            spkr_serials = self.__dict__['speakers']  # <4>
            fetch = self.__class__.fetch  # <5> 클래스 메서두 참조 가져온다
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                                  for key in spkr_serials]  # <6>
        return self._speaker_objs  # <7>

    def __repr__(self):
        if hasattr(self, 'name'):  # <8>
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()  # <9>
# END SCHEDULE2_EVENT


# BEGIN SCHEDULE2_LOAD
def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]  # <1>
        cls_name = record_type.capitalize()  # <2> 클래스 불러오기 위함
        cls = globals().get(cls_name, DbRecord)  # <3> cla_name 클래스가 없다면 DbRecord 불러옴
        if inspect.isclass(cls) and issubclass(cls, DbRecord):  # <4>
            factory = cls  # <5>
        else:
            factory = DbRecord  # <6>
        for record in rec_list:  # <7>
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)  # <8>
# END SCHEDULE2_LOAD

if __name__=='__main__':
    import shelve
    db = shelve.open(DB_NAME)
    if CONFERENCE not in db: load_db(db) # 비어있으면 JSON에서 로드

# BEGIN SCHEDULE2_DEMO

    DbRecord.set_db(db)  # <1> 레코드 들에 대한 DB 매핑에 대한 참조를 전달
    event = DbRecord.fetch('event.33950')  # <2> 특정 레코드를 가져온다
    event  # <3> <Event 'There *Will* Be Bugs'> ; repr 출력시 name을 뱉는다.
    event.venue  # <4> <DbRecord serial='venue.1449'>
    event.venue.name  # <5> 'Portland 251'

    for spkr in event.speakers:  # <6>
        print('{0.serial}: {0.name}'.format(spkr))

    # 잘 빼냈다.
    # speaker.3471: Anna Martelli Ravenscroft
    # speaker.5199: Alex Martelli

# END SCHEDULE2_DEMO

    db.close()