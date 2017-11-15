import http.client,urllib.parse
params = urllib.parse.urlencode({'@number':12345,'@type':'issue','@action':'show'})
headers = {"Content-type":"application/get-photo","Accept":"text/plain"}
conn = http.client.HTTPConnection("127.0.0.1",10000)
conn.request("POST","",params,headers)
response = conn.getresponse()
print(response.status,response.reason,response.headers)
