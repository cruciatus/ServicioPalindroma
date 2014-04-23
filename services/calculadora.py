from ladon.ladonizer import ladonize

class Calculadora(object):
  """
  Este servicio realiza la suma de 2 numeros
  """
  @ladonize(int,int,rtype=int)
  def suma(self,a,b):
    """
    Suma dos enteros y devuelve un resultado

    @param a: 1er entero
    @param b: 2do entero
    @rtype: El resultado de la suma
    """
    return a+b

