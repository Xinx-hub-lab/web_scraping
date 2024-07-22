import scrapy
from ..items import DemoScrapy2Item ## import from item.py


class QuotesspiderSpider(scrapy.Spider):

    name = 'quotesspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    ## starting page
    page_offset = 1

    def parse(self, response):

        # parse single page content
        item = DemoScrapy2Item()
        
        ## direct to quotes
        lst_of_quotes = response.xpath('//div[@class = "quote"]')

        for quote in lst_of_quotes:

            ## extract quote
            content = quote.xpath('./span[@class = "text"]/text()').get()
            ## extract author
            author = quote.xpath('./span/small[@class = "author"]/text()').get()
            ## extract tags
            tag_lst = quote.xpath('./div[@class = "tags"]/a')
            tags = [t.xpath('./text()').get() for t in tag_lst]

            ## assign extracted to item fields
            item['content'] = content
            item['author'] = author
            item['tags'] = tags

            yield item

        
        # go to next page
        if self.page_offset < 10:

            self.page_offset += 1

            ## extract url
            next_page = response.xpath('//nav/ul/li[@class = "next"]/a/@href').get()

            if next_page:
                ## construct the full url
                next_page_url = response.urljoin(next_page)
                ## yield a new request
                yield scrapy.Request(next_page_url, callback=self.parse)
