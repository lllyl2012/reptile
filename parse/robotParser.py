from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.taobao.com/robots.txt')
#rp.read()
print(rp.read())
#print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
#print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))