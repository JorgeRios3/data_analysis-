import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "busqueda"

    #def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #    ]
    #    for url in urls:
    #       yield scrapy.Request(url=url, callback=self.parse_1)
    start_urls = [
        #'http://quotes.toscrape.com/page/1/',
        #'http://quotes.toscrape.com/page/2/',
        'http://books.toscrape.com/'
    ]

    # basic call
    def parse_1(self, response):
        #print(response.body)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        soup = BeautifulSoup(response.body, "html.parser")
        print(soup.find('div', class_='quote'))
        print("---------final de pagina----------")
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    
    # create json file from content
    def parse_2(self, response):
        for quote in response.css('div.quote'):
            valor =  {
                'text': quote.css('span.text::text').get(), #scrapy selectors
                'author': quote.css('small.author::text').get(), #scrapy selectors
                'tags': quote.css('div.tags a.tag::text').getall(), #scrapy selectors
            }
            with open('dictionario.txt', 'w') as f:
                f.write("{}".format(valor))
    
    #crawl into page
    def parse_1(self, response):
        #cachar attributo
        categoria = getattr(self, 'categoria', None)
        print("viendo categoria ----- #{}".format(categoria))
        soup = BeautifulSoup(response.body, "html.parser")
        elemento = soup.find_all('li', class_="next")
        #buscar libro por precio
        print(soup)
        if len(elemento) > 0:
            url = elemento[0].a['href']
            next_page = response.urljoin(url)
            print("next page ", next_page)
            if next_page is not None:
                #yield scrapy.Request(next_page, callback=self.parse)
                yield response.follow(url, callback=self.parse_1)

    # buscar por categoria    
    def parse(self, response):
        categoria = getattr(self, 'categoria', None)
        elemento_busqueda = ""
        soup = BeautifulSoup(response.body, "html.parser")
        lista_categorias = soup.find('div', class_="side_categories")
        lista_categorias = lista_categorias.select('ul > li')
        for elemento in lista_categorias:
            if elemento.a.text.strip() == categoria:
                elemento_busqueda = elemento
        print("elemento de categoria buscada {}".format(elemento_busqueda))
        url = elemento_busqueda.a['href']
        next_page = response.urljoin(url)
        print("pagina de categoria ", categoria,  next_page)
        yield response.follow(url, callback=self.parse_1)




