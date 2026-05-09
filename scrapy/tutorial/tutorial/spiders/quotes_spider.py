import scrapy

class QuotesSpider(scrapy.Spider):
    name = "finca-raiz"

    def start_requests(self):
        urls = []
        for i in range(1, 21):
            urls.append('https://www.fincaraiz.com.co/finca-raiz/arrendamientos/medellin/?ad=30|'+ str(i) +'||||2|||||55|5500006||||||||||||||||1|||1||griddate%20desc||||||/')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'finca-raiz-page-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)