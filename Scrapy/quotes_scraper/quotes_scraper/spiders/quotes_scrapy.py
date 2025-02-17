import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        # Loop through each quote block
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Follow the "Next" page link
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
