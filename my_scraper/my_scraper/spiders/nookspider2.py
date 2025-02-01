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
    start_urls= ['https://books.toscrape.com/']

    def parse(self,response):
        books = response.css("article.product_pod")
        for book in books:
            current_url = response.css("li.next a ::attr(href)").get()
            if 'catalogue/' in current_url:
                next_url = "https://books.toscrape.com/" + current_url
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + current_url
                
            yield response.follow(next_url,callback = self.parse_current_book)
    def parse_current_book(self, response):
        pass 


#scrapy shell "https://books.toscrape.com/"
# books = response.css("article.product_pod") 
#  title = books.css("h3 a::text").get()
#  price = book.css("div.product_price .price_color::text").ge

# link =book.css("h3 a").attrib['href'] 