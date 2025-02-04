import scrapy
from my_scraper9.items import BookItem  
import random

from urllib.parse import urlencode
# ## booksspider.py

API_KEY = 'da27e0ae-d056-45d9-af05-9a255d5f66c5'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com','proxy.scrapeops.io/v1/?']
    start_urls = ['https://books.toscrape.com/']

    # custom_settings = {
    # 'FEEDS': { 'book_data.csv': { 'format': 'csv',}}
    # }
    
    custom_settings = {
        'FEEDS': {
            'booksdata.json': {'format': 'json', 'overwrite': True},
        }
    }


    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)


    def parse_book_page(self, response):
        book = response.css("div.product_main")[0]
        table_rows = response.css("table tr")
        book_item= BookItem()
        book_item['url'] = response.url,
        book_item ['title'] = response.css('.product_main h1::text').get(),
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type']= table_rows[1].css("td ::text").get(),
        book_item['price_excl_tax']= table_rows[2].css("td ::text").get(),
        book_item['price_incl_tax']= table_rows[3].css("td ::text").get(),
        book_item['tax']= table_rows[4].css("td ::text").get(),
        book_item['availability']= table_rows[5].css("td ::text").get(),
        book_item['num_reviews']= table_rows[6].css("td ::text").get(),
        book_item['stars']= response.css("p.star-rating").attrib['class'],
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item['description']= response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item['price']= response.css('p.price_color ::text').get().strip()
        yield book_item
    
#//div[@id="product_description"]/following-sibiling::p/text()")
#//*[@id="default"]/div/div/ul