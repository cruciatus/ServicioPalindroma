from ladon.ladonizer import ladonize

class PalabrasVerificaciones(object):
  """
  Este servicio verifica si una palabra es Palindroma
  """
  @ladonize(str,rtype=str)
  def palindroma(self,palabra):
    """
    Verfica un string y su inversa

    @param palabra: texto ingresado
    @rtype: El resultado del analisis
    """
    frase = palabra    
    #palabra = ''.join(c for c in unicodedata.normalize('NFD', palabra.lower()) if unicodedata.category(c) != 'Mn')
    if " " in palabra:
        texto1 = "La frase ingresada es: "
        palabra = palabra.replace(" ","")
        palabra = palabra.replace(".","")
        palabra = palabra.replace(",","")
        invpalabra = palabra[::-1]
        if palabra == invpalabra:
            texto = "La frase ingresada ES PALINDROMA"
        else:
            texto = "La frase ingresada NO ES PALINDROMA"
    else:
        palabra = palabra.replace(".","")
        palabra = palabra.replace(",","")
        invpalabra = palabra[::-1]

        if palabra == invpalabra:
            texto = "La palabra ingresada ES PALINDROMA"
        else:
            texto = "La palabra ingresada NO ES PALINDROMA"
    return texto

