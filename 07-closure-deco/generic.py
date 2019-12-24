r"""
htmlize(): generic function example

# BEGIN HTMLIZE_DEMO

>>> htmlize({1, 2, 3})  # <1>
'<pre>{1, 2, 3}</pre>'
>>> htmlize(abs)
'<pre>&lt;built-in function abs&gt;</pre>'
>>> htmlize('Heimlich & Co.\n- a game')  # <2> str객체는 <p>로
'<p>Heimlich &amp; Co.<br>\n- a game</p>'
>>> htmlize(42)  # <3> int객체는 10진수 / 16진수로
'<pre>42 (0x2a)</pre>'
>>> print(htmlize(['alpha', 66, {3, 2, 1}]))  # <4> 리스트 항목은 해당 자료형에 따라 포맷팅 그리고 HTML 리스트를 출력
<ul>
<li><p>alpha</p></li>
<li><pre>66 (0x42)</pre></li>
<li><pre>{1, 2, 3}</pre></li>
</ul>

# END HTMLIZE_DEMO
"""

# BEGIN HTMLIZE (범용 함수 작성)

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch  # <1>
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)  # <2>
def _(text):            # <3>
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)  # <4> int의 추상베이스클래스 (for 다형성)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)  # <5> 여러 자료형을 위해 데커레이터 쌓는 것도 가능
@htmlize.register(abc.MutableSequence) # <6> list의 추상베이스클래스 (for 다형성)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

# END HTMLIZE

