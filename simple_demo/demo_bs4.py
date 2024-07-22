
from bs4 import BeautifulSoup

## bs4 for extracting data from wiki:
## https://www.pluralsight.com/resources/blog/guides/extracting-data-html-beautifulsoup

soup = BeautifulSoup(open("beautifulsoup.html"), features = "lxml")
print(soup)
print(type(soup))

## automatic indentation for easy parsing
print(soup.prettify()) 

## get the **first** tag with a 
print(soup.a) 

## get the attributes in tag a printed as dict
print(soup.a.attrs)

## get class list in tag a 
print(soup.a.attrs['class'])

## modify elements, e.g. modify a class
soup.a.attrs['class'] = 'brother'
print(soup.a)

## get text
print(soup.a.string)
print(type(soup.a.string)) ## comment

## get all tags in body
for child in soup.body.children:
    print(child)

## get all strings in body
for str in soup.stripped_strings:
    print(str)

## get all a tags
print(soup.find_all('a')) ## return a list of tags

## more on find_all() function arguments
print(soup.find_all(text = 'Lacie'))
print(soup.find_all(attrs = {"class": "sister"}))


# use CSS selectors, easier to select by attributes or tags
## find all tags as b
soup.select("b")
## find all class = sister
soup.select(".sister")
## find all id = link1
soup.select("#link1")
