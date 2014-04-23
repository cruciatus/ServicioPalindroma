from ladon.ladonizer import ladonize
from ladon.compat import PORTABLE_STRING
from ladon.types.ladontype import LadonType
from decimal import Decimal
import psycopg2



DSN = "dbname=postgres user=postgres password=Diana*0104 host=localhost"

class Materia(LadonType):
    codigo = int
    nombre = PORTABLE_STRING


               
class Alumnos_materias(object):
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
        query = "SELECT materias.cod_materia, materias.nombre_materia FROM estudiantes INNER JOIN matricula ON estudiantes.cod_estudiante = 1401001 AND matricula.est = 1401001 INNER JOIN materias on matricula.mat = materias.cod_materia;" 
        cur.execute(query)
        l_mater = []
        for materia in cur.fetchall():
            e = Materia()
            e.codigo = int(materia[0])
            e.nombre = materia[1]

            l_mater.append(e)
        return l_mater