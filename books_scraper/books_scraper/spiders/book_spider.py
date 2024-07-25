import scrapy
import re
from ..items import BooksScraperItem 


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    ## loop for parsing
    def parse(self, response):

        ## parse category urls on the side bar
        category_pages_lst = response.xpath('//div[@class = "side_categories"]/ul/li/ul/li/a/@href').getall()

        ## click the category
        for category_page in category_pages_lst:
            category_url = response.urljoin(category_page)
            ## turn to parsing category
            yield scrapy.Request(category_url, callback=self.parse_category)


    def parse_category(self, response):

        ## parse books urls
        book_pages_lst = response.xpath('//ol/li/article/div[@class = "image_container"]/a/@href').getall()
        
        ## click the book image and direct to detailed webpage
        for book_page in book_pages_lst:
            next_page_url = response.urljoin(book_page)
            ## turn to parsing book
            yield scrapy.Request(next_page_url, callback=self.parse_book)
        
        ## go to the next page if exists
        next_page = response.xpath('//li[@class = "next"]/a/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse_category)
    
    
    def parse_book(self, response):
        ## import to store data
        item = BooksScraperItem()

        ## parse the book page
        item['title'] = response.xpath('//h1/text()')\
            .get()
        item['price_pound'] = response.xpath('//p[@class = "price_color"]/text()')\
            .get().replace('£', '').strip()
        item['rating'] = response.xpath('//*[contains(@class, "star-rating")]/@class')\
            .get().split(' ')[-1]
        
        ## get availability
        availability_txt = response.xpath('//p[@class = "instock availability"]/text()').getall() 
        ## availability_txt would be ['\n    ', ' In stock (1 available) ', '\n'] alike
        availability_txt = ''.join(availability_txt).strip()
        ## extract instock number
        availability_number = re.findall(r'\d+', availability_txt)
        item['availability'] = availability_number[0] if availability_number[0] else '0'
        ## return in stock yes or no
        item['in_stock'] = 'yes' if 'In stock' in availability_txt else 'no'
        
        ## get book description
        item['description'] = response.xpath('//div[@id = "product_description"]/following-sibling::p/text()').get()

        ## get book category
        item['category'] = response.xpath('//ul[@class = "breadcrumb"]/li[3]/a/text()').get()

        yield item