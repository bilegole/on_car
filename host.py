import wsgiref.simple_server
import multiprocessing
import main


LOCALHOST = ''
DEFAULT_PORT = 10004

def run(url,port):
    httpd = wsgiref.simple_server.make_server(url,port,application)
    print('服务器启动成功。。。')
    httpd.serve_forever()



def application(env,res):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    print('123456789')
    head = sorted(env.items())
    for k,v in head:
        print( k , '     \t' , v , '\n')
    request_body = env['wsgi.input'].read(request_body_size)
    print(request_body)
    with open('/Users/yuyang/tttttttttt/2.jpge','wb') as f:
        f.write(request_body)
    res('200 OK',[('Content-Type', 'text/html')])
    print('111')
    main.q.put(request_body)
    #print(env['wsgi.input'].read())
    return [b'<h1>Hello, web!</h1>']

host = multiprocessing.Process(target=run,args=(LOCALHOST,DEFAULT_PORT))
#run(LOCALHOST,DEFAULT_PORT)
host.start()
