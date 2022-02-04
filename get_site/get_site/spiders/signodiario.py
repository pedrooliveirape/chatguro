import scrapy


class SignodiarioSpider(scrapy.Spider):
    cont = 0
    name = 'signodiario'
    start_urls = [f'http://www.horoscopovirtual.com.br/horoscopo/aries']
    lista_signos = ('aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario',
                    'capricornio', 'aquario', 'peixes')

    def parse(self, response):
        yield {
            SignodiarioSpider.lista_signos[SignodiarioSpider.cont]: response.xpath("*//p[@class='text-pred']/text()").getall()
        }
        SignodiarioSpider.cont += 1
        prox_signo = f'/horoscopo/{SignodiarioSpider.lista_signos[SignodiarioSpider.cont]}'
        if SignodiarioSpider.cont <= len(SignodiarioSpider.lista_signos):
            yield response.follow(prox_signo, callback=self.parse)


class Signosemanal(scrapy.Spider):
    cont = 0
    name = 'signosemanal'
    start_urls = [f'https://www.horoscopovirtual.com.br/horoscopo-semanal/aries']

    def parse(self, response):
        lista_signos = ('aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario',
                    'capricornio', 'aquario', 'peixes')

        yield {
            'semana': response.xpath('//*[@id="content"]/section/article/div/h2/strong/text()').get(),
            lista_signos[Signosemanal.cont]: response.xpath('.//p[@class="text-pred"]/text()').getall()[0]
        }
        Signosemanal.cont += 1
        if Signosemanal.cont < len(lista_signos):
            prox_signo = f'horoscopo-semanal/{lista_signos[Signosemanal.cont]}'
            yield response.follow(prox_signo, callback=self.parse)