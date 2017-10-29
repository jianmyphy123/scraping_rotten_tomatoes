import scrapy

from rt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    name = 'RottenTomatoes'
    allowed_domains = ['rottentomatoes.com']
    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/?year=2017'
    ]

    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath('./td[3]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        item = RTItem()
        item['title'] = response.xpath('//*[@id="heroImageContainer"]/a/h1/text()')[0].extract().strip()
        item['score'] = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()')[0].extract()
        item['genres'] = response.xpath('//*[@id="mainColumn"]/section[3]/div/div/ul/li[2]/div[2]//a/text()').extract()
        consensus_list = response.xpath('//*[@id="all-critics-numbers"]/div/div[2]/p/text()').extract()[1:]
        item['consensus'] = ''.join(consensus_list).strip()
        yield item
