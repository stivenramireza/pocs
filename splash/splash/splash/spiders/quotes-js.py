import scrapy
from scrapy_splash import SplashRequest
import scrapy_proxies


class QuotesJSSpider(scrapy.Spider):
    name = 'anutibara'
    # all these settings can be put in your project's settings.py file
    start_urls = []
    custom_settings = {
        'SPLASH_URL': 'http://localhost:8050',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
    }

    def start_requests(self):
        urls = [
            'https://anutibara.com/propiedades?oferta=Arrendamiento&pagina=1&rango[]=100000&rango[]=1500000'
        ]
        for url in urls:
            yield SplashRequest(url, self.parse,  args={'wait': 8})

    def parse(self, response):
        filename = 'anutibara.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)