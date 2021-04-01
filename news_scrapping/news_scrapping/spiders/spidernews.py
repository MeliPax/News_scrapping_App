import scrapy
from ..items import NewsMiningItem


class NbcSpider(scrapy.Spider):
    name = 'news_crawler'
    start_urls = ['https://abcnews.go.com/Entertainment']

    def parse(self, response, **kwargs):
        items = NewsMiningItem()

        link = response.css('.ContentRoll__Headline h2 a::attr(href)').extract()

        print(len(link))
        title = response .css('.ContentRoll__Headline h2 a::text').extract()
        print(len(title))
        category = response.css('div.css-10wtrbd span.eyebrow a span::text').extract()
        print(len(category))
        items['link'] = link
        items['title'] = title
        items['category'] = category
        yield items
        # yield {'link': link, 'title': title, 'category': category}
