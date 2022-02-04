import scrapy

class Signosemanal(scrapy.Spider):
    cont = 0
    name = 'signosemanal'
    start_urls = [f'https://www.horoscopovirtual.com.br/horoscopo-semanal/aries']

    def parse(self, response):
        lista_signos = ('aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario',
                    'capricornio', 'aquario', 'peixes')

        yield {
            'semana': response.xpath('//*[@id="content"]/section/article/div/h2/strong/text()').get(),
            lista_signos[Signosemanal.cont]: response.xpath('.//p[@class="text-pred"]/text()').getall()[0],
            'amor': response.xpath('.//p[@class="text-pred"]/text()').getall()[1],
            'trabalho': response.xpath('.//p[@class="text-pred"]/text()').getall()[2]
        }
        Signosemanal.cont += 1
        prox_signo = f'{lista_signos[Signosemanal.cont]}'
        if Signosemanal.cont <= len(lista_signos):
            yield response.follow(prox_signo, callback=self.parse)