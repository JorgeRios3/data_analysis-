# pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

#base_url = 'http://quotes.toscrape.com/page/1/'
base_url = 'https://www.lustmexico.com/'
#base_url = 'http://127.0.0.1:5000/'
with requests.Session() as session:  # maintaining a web-scraping session
    soup = BeautifulSoup(session.get(base_url).content, "html.parser")
    #soup.p.string.wrap(soup.new_tag("b"))
    #a_tag.i.unwrap()

    #prettify()

    #primer elemento <span>
    #print(soup.div)

    #obtener texto de el elemento
    #print(soup.div.h1.text)

    #modificar texto del elemento
    #elemento = soup.div.h1
    #elemento.string = "mi parte del titulo {}".format(elemento.text)
    #print(elemento)

    #agegar elemento a otro elemento
    #elemento = soup.div.h1
    #elemento = "<div id='new_div'>{}</div>".format(elemento)
    #print(elemento)

    #primer elemento de eqitueta >span>
    #print(soup.span)

    #primer elemento <span> que se encuentre dentro de un <div> directamente
    #print(soup.div.span)

    # todos los elementos de etiqueta div
    #print(soup.select('div'))
    #print(soup.find_all('div'))

    #obtener elementos de etiqueta a y h1
    #print(soup.find_all(["a", "h1"]))

    # elemento con atributo id = label_nombre
    #print(soup.select('#pi-american_express'))
    #print(soup.find(id="pi-master"))

    # todos los elementos con clase .qoute
    #print(soup.select('.quote'))
    #print(soup.find_all(class_="quote"))
    #print(soup.find_all('div', class_="quote"))

    # elemento con clase=tag y valor href=/tag/world/page/1/
    #print(soup.find(class_="tag", href="/tag/world/page/1/"))

    # todos los elementos <span> que esten dentro de un <div>
    #print(soup.select('div span'))
    
    # todos los elementos <span> que esten dentro de un <div> directamente, sin ningun otro elemento en medio
    #print(soup.select('nav > ul'))

    #obtener padre del elemento
    #print(soup.h1.parent)
    #print(soup.h1.parent.name) 

    
    # LUST
    # todos los elementos <input> que tengan el atributo name (este es el atributo default name) sin inportar el valor
    #print(soup.select('input[type]'))

    # todos los elementos <input> que tengan el  atributo llamado type con el valor seach
    #print(soup.select('input[type="search"]'))
    
    #agregar o modificar attributo del elemento
    #elemento = soup.select('input[type="search"]')
    #elemento[0]['id']= "input_search"
    #elemento[0]['name']="new_name"
    #print(elemento)

    #borrar atributo del elemento
    #elemento = soup.select('input[type="search"]')
    #del elemento[0]['name']
    #print(elemento)


    #elemento = soup.find_all('li', class_="next")
    #elemento = elemento[0]
    #print(elemento.a['href'])
    



