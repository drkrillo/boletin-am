from bs4 import BeautifulSoup
import requests

NORMAS = [
    "ACORDADAS",
    "ASOCIACIONES SINDICALES",
    "AUDIENCIAS PÚBLICAS",
    "AVISOS OFICIALES",
    "CONCURSOS OFICIALES",
    "CONVENCIONES COLECTIVAS DE TRABAJO",
    "DECISIONES ADMINISTRATIVAS",
    "DECRETOS",
    "DECRETOS DESCLASIFICADOS",
    "DISPOSICIONES",
    "DISPOSICIONES CONJUNTAS",
    "DISPOSICIONES SINTETIZADAS",
    "FALLOS",
    "INSTRUCCIONES PRESIDENCIALES",
    "INSTRUCCIONES GENERALES",
    "LEGISLACION",
    "LEYES",
    "REMETAS OFICIALES",
    "RESOLUCIONES",
    "RESOLUCIONES CONJUNTAS",
    "RESOLUCIONES GENERALES",
    "RESOLUCIONES SINTETIZADAS",
    "SENTENCIAS",
    "TRATADOS Y CONVENIOS INTERNACIONALES",
]

BASE_URL = 'https://www.boletinoficial.gob.ar/detalleAviso/primera/'


class BoletinScraper(object):
    """
    Scrapper class for Boletin Oficial.
    """
    def __init__(
        self, 
        date: str,
        id: int,
    ):
        self.date = date
        self.id = id
        self.url =f"{BASE_URL}{str(self.id)}/{self.date}"
    
    def scrape(self):
        """
        Scrapes article from Boletin Oficial.
        Returns dict with:
        * Date
        * ID
        * Content
        * Link
        * Summary (empty, will be filled)
        """
        page = requests.get(self.url)
        print(self.url)
        soup = BeautifulSoup(page.content, "html.parser")

        content = soup.find(id="detalleAviso").text

        parsed_article = {
            'date': self.date,
            'url': self.url,
            'content': content,
            'summary': None,
        }

        return parsed_article
