import scrapy
from ..items import BooksScraperItem 


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    ## loop for parsing
    def parse(self, response):

        ## import to store data
        item = BooksScraperItem()
        
        ## click the category
        category_page = response.xpath().get()
        category = response.xpath().get()
        if category_page:
            next_page_url = response.urljoin(category_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

            ## assign category
            item['tags'] = category

            ## click a book
            book_page = response.xpath().get()
            if category_page:
                next_page_url = response.urljoin(category_page)
                yield scrapy.Request(next_page_url, callback=self.parse)

                ## parse the book page
                title = response.xpath().get()
                price_pound = response.xpath().get()
                rating = response.xpath().get()
                avaibility = response.xpath().get()
                in_stock = response.xpath().get()
                description = response.xpath().get()

            ## go back
            next_page = response.xpath().get()
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
        
            ## go to the next page
            next_page = response.xpath().get()
            if category_page:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)

            ## click the next category
            if category_page:
                next_page_url = response.urljoin(category_page)
                yield scrapy.Request(next_page_url, callback=self.parse)
