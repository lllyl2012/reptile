import socket
import urllib.request
import urllib.error

url = 'http://lllyl2012.top'
headers = {
	'User-Agent':'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)',
	'Host':'lllyl2012.top'
}
dict = {
	'username':'demo',
	'password':'123'
}
data = bytes(urllib.parse.urlencode(dict),encoding='utf8')
try:
	request = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
	response = urllib.request.urlopen(request)
	print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
	if isinstance(e.reason, socket.timeout):
		print('time out')

