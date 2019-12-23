

"""
# BEGIN TAG_DEMO
>>> tag('br')  # <1> Case1의 경우
'<br />'
>>> tag('p', 'hello')  # <2> Case2의 경우
'<p>hello</p>'
>>> print(tag('p', 'hello', 'world'))
<p>hello</p>
<p>world</p>
>>> tag('p', 'hello', id=33)  # <3> 명시적으로 이름이 지정되지 않은 kargs는 **attr이 잡는다.
'<p id="33">hello</p>'
>>> print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
<p class="sidebar">hello</p>
<p class="sidebar">world</p>
>>> tag(content='testing', name="img")  # <5> 명시적으로 이름이 지정되지 않은 kargs는 **attr
'<img content="testing" />'
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
...           'src': 'sunset.jpg', 'cls': 'framed'}
>>> tag(**my_tag)  # <6> 딕셔너리에 **을 붙이면 모든 항목을 argument로 전달
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

# END TAG_DEMO
"""


# BEGIN TAG_FUNC
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs: # Case1 : 키워드 전용 매개변수가 들어온다면(안에서는 딕셔너리)
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content: # Case2 : 위치매개변수가 들어온다면(안에서는 튜플)
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else: # Case3 : name만 들어온다면
        return '<%s%s />' % (name, attr_str)
# END TAG_FUNC

def test(name, **kwargs):
    print(name)
test(111)
test(**{'name': 111}) # 딕셔너리에 **을 붙이면 모든 항목을 argument로 전달

