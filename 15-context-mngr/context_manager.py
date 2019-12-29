with open('mirror.py') as fp:
    src = fp.read(60)

len(src) # 60
fp # <_io.TextIOWrapper name='mirror.py' mode='r' encoding='cp949'>
fp.closed, fp.encoding # (True, 'cp949')
fp.read(60) # 더이상 파일 입출력은 할 수 없다


from mirror import LookingGlass
with LookingGlass() as what:
    print('ABCDEFG') # GFEDCBA; 역순
    print(1/0)
    print(what) # YKCOWREBBAJ; 역순
print(what) # JABBERWOCKY; 정상


# with 문 없이도 컨텍스트 매니저를 사용할 수 있다
from mirror import LookingGlass
manager = LookingGlass()  # <1>
manager
monster = manager.__enter__()  # <2>
monster == 'JABBERWOCKY'  # <3> eurT ; 여기서 출력함수가 멍키패칭됨

monster #'YKCOWREBBAJ

manager.__exit__(None, None, None)  # <4>
monster # 'JABBERWOCKY'; 출력함수 정상