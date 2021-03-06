from ladon.ladonizer import ladonize
from ladon.compat import PORTABLE_STRING
from ladon.types.ladontype import LadonType
from decimal import Decimal
import psycopg2


#datos = [(Decimal('1401001'), 'JUAN', 'JOSE', 'PEREZ', 'PAEZ', Decimal('25'), 'jperez@gmail.com', Decimal('3187654234')),
#(Decimal('1401002'), 'ASTRID', 'MARIA', 'HERNANDEZ', 'SOTO', Decimal('23'), 'amhernandez@gmail.com', Decimal('3118976543')),
#(Decimal('1401003'), 'ANDRES', None, 'PAEZ', 'CASTRO', Decimal('27'), 'apez@gmail.com', Decimal('3126547893'))]

DSN = "dbname=postgres user=postgres password=Diana*0104 host=localhost"

class Estudiante(LadonType):
    codigo = int
    nombre_1 = PORTABLE_STRING
    nombre_2 = {"type":PORTABLE_STRING, "nullable": True}
    apellido_1 = PORTABLE_STRING
    apellido_2 = PORTABLE_STRING
    correo = PORTABLE_STRING

               
class Mat_estudiantes(object):
    """
    Este servicio se conecta a una base datos en postgresql
    """
    @ladonize(rtype=[Estudiante])
    def leer_datos(self):
        """
        Se conecta a la base de datos y realiza la consulta de los alumnos
        @param palabra: texto ingresado
        @rtype: El resultado del analisis
        """
        con = psycopg2.connect(DSN)
        cur = con.cursor()
        query = "SELECT estudiantes.cod_estudiante, estudiantes.primer_nombre, estudiantes.segundo_nombre, estudiantes.primer_apellido, estudiantes.segundo_apellido, estudiantes.correo_electronico FROM estudiantes INNER JOIN matricula ON estudiantes.cod_estudiante = matricula.est AND matricula.mat = 1203;"
        cur.execute(query)
        l_estudiantes = []

        for estudiante in cur.fetchall():
            e = Estudiante()
            e.codigo = int(estudiante[0])
            e.nombre_1 = estudiante[1]
            e.nombre_2 = estudiante[2]
            e.apellido_1 = estudiante[3]
            e.apellido_2 = estudiante[4]
            e.correo = estudiante[5]
            l_estudiantes.append(e)
        return l_estudiantes