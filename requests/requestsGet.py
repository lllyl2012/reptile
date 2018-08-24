import requests
import re

data = {
	'name':'tom',
	'age':22
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',params=data,headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
#print(type(r))
#print(r.status_code)
#print(type(r.text))
#print(r.text)
#print(r.cookies)
#print(r.json())