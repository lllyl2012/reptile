from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
#result = html.xpath('//*')
#result = html.xpath('//li/a')
#result = html.xpath('//ul//a')
#result = html.xpath('//a[@href="link4.html"]/../@class')
#result = html.xpath('//li[@class="item-0"]/a/text()')
#result = html.xpath('//li/a/@href')
#result = html.xpath('//li[contains(@class,"li")]/a/text()')
#result = html.xpath('//li[contains(@class,"li") and @name="gaga"]/a/text()')
#result = html.xpath('//li[1]/a/text()')
#result = html.xpath('//li[last()]/a/text()')
#result = html.xpath('//li[position()<3]/a/text()')
#result = html.xpath('//li[last()-2]/a/text()')

#result = html.xpath('//li[1]/ancestor::*')
#result = html.xpath('//li[1]/ancestor::div')
#result = html.xpath('//li[1]/attribute::*')
#result = html.xpath('//li[1]/child::a[@href="link1.html"]')
#result = html.xpath('//li[1]/descendant::span')
#result = html.xpath('//li[1]/following::*[2]')#当前节点之后的所有节点，包括子节点和同级节点
#result = html.xpath('//li[1]/following-sibling::*')#当前节点之后所有同级节点
print(result)