
import requests
from bs4 import BeautifulSoup
import pandas as pd

## fetch html 
url = 'https://quotes.toscrape.com/'
html_content = requests.get(url).text

## parse html contents
soup = BeautifulSoup(html_content, "lxml")

## extract author and quotes
## method 1, css select
sentence_lst = [sentence.text for sentence in soup.select(".text")]
author_lst = [author.text for author in soup.select(".author")]

## method 2, find_all
sentence_lst = [sentence.text for sentence in soup.find_all(attrs={'class': 'text'})]
author_lst = [author.text for author in soup.find_all(attrs={'class': 'author'})]

## show
df_quote = pd.DataFrame({'Author': author_lst,
                         'Quote': sentence_lst})
print(df_quote)