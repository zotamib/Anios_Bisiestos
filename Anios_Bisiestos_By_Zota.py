#!/usr/bin/python

#UTILIZA ESTE SCRIPT PARA CALCULAR LOS ANIOS BISIESTOS ENTRE 1950 Y 2050.
#Support zuno_systems@hotmail.com
#Powered By Zota.

def bisiesto_1950_2050(anio_de_inicio):

	Zota = anio_de_inicio

	Jenny = anio_de_inicio + 101

	while Zota<Jenny:

	 if Zota%4 == 0 and Zota%100 != 0 or Zota%400 == 0:

		print Zota

	 Zota += 1

bisiesto_1950_2050(1950)
