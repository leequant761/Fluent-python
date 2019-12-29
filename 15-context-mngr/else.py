# else라 쓰고 then이라 읽는다.

# for,while 루프가 완전히 실행된 후에(break 걸리면 안됨) else 블록 실행
for item in [1, 2, 3, 4]:
    if item == 5:
        break
else:
    raise ValueError('No 5 found')

# try 블록에서 예외가 발생하지 않으면 else블록으로 실행(else블록 예외는 except가 안잡음)
import random

def dangerous_call():
    if random.randint(1,3) == 3:
        raise OSError

def after_call():
    print('Success')

# try:
#     dangerous_call() # 위험한 요청
#     after_call() # 위험한 요청이 예외가 발생하지 않으면 실행
# except OSError:
#     print('OSError')

# 이게 더 좋은 코드(의도를 명확히 할 수 있다; try블록에서 어떤 함수에서의 에러를 처리하기 위한 것인 지 보임)
try:
    dangerous_call() # 위험한 요청
except OSError:
    print('OSError')
else:
    after_call() # 위험한 요청이 예외가 발생하지 않으면 실행
