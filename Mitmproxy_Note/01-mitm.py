from mitmproxy import http
from mitmproxy.http import Request
from mitmproxy.http import HTTPFlow
from mitmproxy.http import Response


def request(flow: http.HTTPFlow):
    print('请求->', flow.request.url)
    print('请求->', flow.request.host)
    print('请求->', flow.request.path)
    print('请求->', flow.request.query)
    print('请求->', flow.request.cookies)
    print('请求->', flow.request.headers)
    print('请求->', flow.request.method)
    print('请求->', flow.request.content)


def response(flow: http.HTTPFlow):
    print(flow.request.url)

    print(flow.response.status_code)
    print(flow.response.cookies)
    print(flow.response.headers)
    print(flow.response.content)
    print(flow.response.text)
    print(flow.response.json())

# python环境配置
# pip install mitmproxy

# 启动(-p:代表端口 -s:运行的脚本)
# mitmdump -q -p 8888 -s 01-mitm.py
# 默认在系统目录的指定位置生成证书 .mitmproxy文件中(C:\Users\24830\.mitmproxy)
