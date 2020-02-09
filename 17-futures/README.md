# Futures

쉽게 말해서 work thread(process)의 핸들이라고 볼수 있다. 

`future.result()`를 통해 threadpool에 보낸 함수의 결과를 받을 수 있다.

함수가 에러가 생기면 `future.result()`을 실행할 때 exception을 발생시킨다.

```python
from concurrent import futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://some-made-up-domain.com/']

def load_url(url, timeout):
    return urllib.request.urlopen(url, timeout=timeout).read()

def main():
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        # excutor.submit()으로 thread pool에서 돌릴 함수를 등록하면 
        # future(키) url(값)를 리턴한다.
        # 등록된 함수(load_url)는 thread pool에서 비동기로 실행된다.
        future_to_url = dict((executor.submit(load_url, url, 60), url) for url in URLS)
		# 아래의 제너레이터는 웹에서 다운로드가 다 됐을 때마다 하나씩 future키를 뱉는다.
        for future in futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                print('%r page is %d bytes' % (
                          url, len(future.result())))
            except Exception as e:
                print('%r generated an exception: %s' % (
                          url, e))

if __name__ == '__main__':
    main()
```

