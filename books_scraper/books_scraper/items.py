# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    price_pound = scrapy.Field()
    rating = scrapy.Field()
    avaibility = scrapy.Field()
    in_stock = scrapy.Field()
    description = scrapy.Field()
