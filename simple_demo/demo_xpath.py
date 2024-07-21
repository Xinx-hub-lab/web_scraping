
import lxml
from lxml import etree

html = etree.parse('xpath.html')
print(html)

# get text

## method 1:
## lst of all txt with the path
html_data = html.xpath('/html/body/div/ul/li/a')
for i in html_data:
    print(i.text)

## method 2: use text()
html_data = html.xpath('/html/body/div/ul/li/a/text()')
for i in html_data:
    print(i)

## method 3: easier method
html_data = html.xpath('//li/a/text()')
for i in html_data:
    print(i)


# get href
html_data = html.xpath('//li/a/@href')
for i in html_data:
    print(i)


# get class
html_data = html.xpath('//li/a/@class') ## //li/@class also work
for i in html_data:
    print(i)


# get specific href text
html_data = html.xpath('//li/a[@href = "link2.html"]')  ## note there is no / between 'a' and '[', it should be double quote in sigle quote
for i in html_data:
    print(i.text)

# get specific class name coresponding text
html_data = html.xpath('//li[@href = "link2.html"]/a/text()') ## it should be double quote in sigle quote
html_data


# get the last text
html_data = html.xpath('//li[last()]/a/text()') 
html_data




## example 2
text = '''
<li class = "zxc asd wer" name = '222'><a href = "link1.html">1 item</a></li>
<li class = "bnm zxc jkl" name = '111'><a href = "link2.html">2 item</a></li>
'''
html = etree.HTML(text)
html_data = html.xpath('//li[contains(@class, "zxc") and @name = "111"]/a/text()') ## it should be double quote in sigle quote
for i in html_data:
    print(i)