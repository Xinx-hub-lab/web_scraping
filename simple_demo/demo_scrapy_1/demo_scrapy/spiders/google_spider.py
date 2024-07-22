import scrapy


class GoogleSpiderSpider(scrapy.Spider):
    name = 'google_spider'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']

    def parse(self, response):
        title = response.xpath('//html/head/title/text()').extract_first()  ## get() also works
        print('Google front page title is ', title)
