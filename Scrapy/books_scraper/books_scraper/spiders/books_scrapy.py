import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        # Extract book details
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('.price_color::text').get(),
                'availability': book.css('.availability::text').re_first('\S+'),
            }

        # Follow pagination links
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
