from pyquery import PyQuery as pq
import requests

doc = pq(requests.get('http://cuiqingcai.com').text)
#doc = pq(filename='demo.html')
print(doc('title'))