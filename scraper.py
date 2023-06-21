from bs4 import BeautifulSoup
import requests


def scrape(article_url):
    """
    Scrapes article from Boletin Oficial.
    Returns Content.
    """
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")

    content = soup.find(id="detalleAviso").text

    return content
