# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         "https://quotes.toscrape.com/page/1/",
#     ]

#     def parse(self, response):
#         for quote in response.css("div.quote"):
#             yield {
#                 "text": quote.css("span.text::text").get(),
#                 "author": quote.css("span small::text").get(),
#                 "tags": quote.css("div.tags a.tag::text").getall(),
#             }

#         next_page = response.css("li.next a::attr(href)").get()
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domain = ['books.toscrape.com']
    start_url = ['https://books.toscrape.com/']

    def parse(self,response):
        pass 
        
#scrapy shell "https://books.toscrape.com/"
# books = response.css("article.product_pod") 
#  title = books.css("h3 a::text").get()
