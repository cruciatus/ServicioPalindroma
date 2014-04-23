from ladon.ladonizer import ladonize
from ladon.compat import PORTABLE_STRING
from ladon.types.ladontype import LadonType
from decimal import Decimal
import psycopg2



DSN = "dbname=postgres user=postgres password=Diana*0104 host=localhost"

class Materia(LadonType):
    codigo = int
    nombre = PORTABLE_STRING
    intensidad = int


               
class Asignatura(object):
    """
    Este servicio se conecta a una base datos en postgresql
    """
    @ladonize(rtype=[Materia])
    def leer_datos(self):
        """
        Se conecta a la base de datos y realiza la consulta de las materias
        @param palabra: texto ingresado
        @rtype: El resultado del analisis
        """
        con = psycopg2.connect(DSN)
        cur = con.cursor()
        query = "SELECT * FROM materias;"
        cur.execute(query)
        l_materias = []

        for materia in cur.fetchall():
            e = Materia()
            e.codigo = int(materia[0])
            e.nombre = materia[1]
            e.intensidad = int(materia[2])

            l_materias.append(e)
        return l_materias