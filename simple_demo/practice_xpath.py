
import requests
import lxml
from lxml import html
import pandas as pd

## fetch html 
url = 'https://quotes.toscrape.com/'
html_content = requests.get(url).text

## parse html contents
tree = html.fromstring(html_content)

## extract author and quotes
sentence_lst = tree.xpath('//div[@class="quote"]/span[@class="text"]/text()')
author_lst = tree.xpath('//div[@class="quote"]/span/small[@class="author"]/text()')

## show
df_quote = pd.DataFrame({'Author': author_lst,
                         'Quote': sentence_lst})
print(df_quote)







