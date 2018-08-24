import socket
import urllib.request
import urllib.error
 
try:
    response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
	print(type(e.reason))
	if isinstance(e.reason, socket.timeout):
		print('TIME OUT')
	else:
		print(e.reason)
else:
    print('Request Successfully')