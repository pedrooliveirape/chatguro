import scrapy


class HoroscopovirtualSpider(scrapy.Spider):
    name = 'horoscopovirtual'
    start_urls = ['https://www.horoscopovirtual.com.br/horoscopo/aquario/']


    def parse(self, response):
        yield{
            'aquario': response.xpath("*//p[@class='text-pred']/text()").getall()
        }

        lista = ('aquario', 'aries', 'cancer', 'capricornio', 'escorpiao', 'gemeos', 'leao', 'libra', 'peixes', 'sagitario',
                 'touro', 'virgem')


