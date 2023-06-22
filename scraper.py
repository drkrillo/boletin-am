from bs4 import BeautifulSoup
import requests


def scrape(article_url):
    """
    Scrapes article from Boletin Oficial.
    Returns Content.
    """
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")

    type = soup.find(id="tituloDetalleAviso")
    type = type.find("h1").text
    content = soup.find(id="cuerpoDetalleAviso").text

    return type, content
