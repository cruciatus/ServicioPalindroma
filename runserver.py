# -*- coding: utf-8 -*-
from ladon.server.wsgi import LadonWSGIApplication
import wsgiref.simple_server
from os.path import abspath,dirname,join

scriptdir = dirname(abspath(__file__))
service_modules = ['calculadora','palindromas']

# Create the WSGI Application
application = LadonWSGIApplication(
	service_modules,
	[join(scriptdir,'services'),join(scriptdir,'appearance')],
	catalog_name = 'Servicios en Ladon',	
	catalog_desc = 'Los siguientes son los servicios existentes')

if __name__=='__main__':
	# Starting the server from command-line will create a stand-alone server on port 8080
	port = 8081
	print("\nLos servicios se estan ejecutando en el puerto %(port)s.\nVer API navegable en http://localhost:%(port)s\n" % {'port':port})

	server = wsgiref.simple_server.make_server('', port , application)
	server.serve_forever()
