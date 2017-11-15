from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:

def application(environ, start_response):
    print('受到访问。。。。')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# 创建一个服务器，IP地址为空，端口是10002，处理函数是application:
httpd = make_server('', 10002, application)
print('Serving HTTP on port 10002...')
# 开始监听HTTP请求:
httpd.serve_forever()

