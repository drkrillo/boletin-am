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


class BoletinObject(object):
    """
    Boletin Oficial article object.
    Attributes:
    * Date: YYYYMMDD
    * ID
    * URL
    * Content
    * Summary
    """
    def __init__(
        self, 
        date: object,
        id: int,
    ):
        self.date = date
        self.id = id
        self.url = f"{BASE_URL}{str(self.id)}/{self.date.strftime('%Y%m%d')}"
        self.type = None
        self.content = None
        self.summary = None