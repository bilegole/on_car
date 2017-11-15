import http.client
import base64
import multiprocessing



LOCALHOST = '127.0.0.1'
DEFAULT_PORT = 10004
q = multiprocessing.Queue()


def get_photo():
    with open('/Users/yuyang/tttttttttt/1.jpge','rb') as f:
        photo = f.read()
    return photo


def send_photo(photo,url,port):
    time_of_photo = '2017-11-12-06-00-0'
    #photo64 = base64.b64encode(photo)
    #print(photo64)
    a = http.client.HTTPConnection(url,port)
    #a.connect()
    headers = {'Content-Type':'photo',}
    a.request('POST',url,'',headers)
    q.close()


#send_photo(get_photo(),LOCALHOST,DEFAULT_PORT)
photo64 = base64.b64encode(get_photo())
print(photo64)
a=http.client.HTTPConnection(LOCALHOST,DEFAULT_PORT)
headers = {'Content-Type':'photo'}
print('1')
a.request('PUT',"",get_photo(),headers)
print('2')
b = a.getresponse()
a.close()
