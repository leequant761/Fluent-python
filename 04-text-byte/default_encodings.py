import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

# locale.getpreferredencoding() -> 'cp949'
#                  type(my_file) -> <class '_io.TextIOWrapper'>
#               my_file.encoding -> 'cp949'
#            sys.stdout.isatty() -> False
#            sys.stdout.encoding -> 'UTF-8'
#             sys.stdin.isatty() -> False
#             sys.stdin.encoding -> 'utf-8'
#            sys.stderr.isatty() -> False
#            sys.stderr.encoding -> 'UTF-8'
#       sys.getdefaultencoding() -> 'utf-8' # 이진데이터 => str 때 디코딩에 사용
#    sys.getfilesystemencoding() -> 'utf-8' # open(파일명(str)) 일 때 디코딩에 사용

# 파일을 열 때 encoding 인수를 생략하면 기본 인코딩 방식이 설정된다.
# 그러니 윈도우에서 파일 입출력에서는 encoding UTF-8을 신경쓰도록하자.