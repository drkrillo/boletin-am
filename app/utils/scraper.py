from bs4 import BeautifulSoup
import requests

def today_urls():
    """
    Returns a list of ids that correspond
    to that day's publications.
    """
    base_url = 'https://www.boletinoficial.gob.ar'
    articles_url = base_url + '/seccion/primera'

    page = requests.get(articles_url)
    soup = BeautifulSoup(page.content, "html.parser")
    body = soup.find(id='avisosSeccionDiv')

    urls = [
        base_url + a['href']
        for a in body.find_all("a", href=True)
    ]

    return urls

def scrape_article(article_url):
    """
    Scrapes article from Boletin Oficial.
    Returns Type, Content and Date.
    """
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")

    type = soup.find(id="tituloDetalleAviso")
    type = type.find("h1").text

    content = soup.find(id="cuerpoDetalleAviso").text

    date = article_url[-8:]

    return type, content, date

