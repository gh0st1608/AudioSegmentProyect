#!/usr/bin/env python3.6

import pysftp
import logica
import os
#from pydub import AudioSegment
from datetime import date
import time

cnopts = pysftp.CnOpts()
cnopts.hostkeys= None  
#inicio del contador
inicio_de_tiempo = time.time()

#credenciales
Host = "190.105.250.103"
User = "root"
Pass = "fr4v4t3l$2020$$"

fecha_hoy = date.today()

dia = fecha_hoy.strftime('%d')
mes = fecha_hoy.strftime('%m')
anio = fecha_hoy.strftime('%Y')
path_local = '/home/audios_fravatel/'
path_audios = '/var/spool/asterisk/monitor/'
path_audios_2 = path_audios + anio + '/' + mes 
#conexion conectora al servidor fravatel o remoto
with pysftp.Connection(host=Host, username = User, password = Pass, port=1610,cnopts=cnopts) as sftp:
	print ("Con est")

	for n in range(1,int(dia)):
		if (int(n)) < 2:
			fecha_dia = '0'+ str(int(n))
			path_audios_3 = path_audios_2 + '/' + fecha_dia + '/'
			#Cambiar a directorio remoto
			sftp.cwd(path_audios_3)
			#sftp.pwd-> indica la ruta absoluta del directorio
			# Obtener estructura del directorio
			lista = sftp.listdir_attr()
			#cantidad de elementos por carpeta(dia-> 01,02,03...31) del mes
			cont_archivos = len(lista)
			for attr in lista:
					#path_audios_4=path_audios_3 + attr.filename
					tam_arreglo = sftp.stat(attr.filename).st_size
					if tam_arreglo > 4000000:
						#ruta absoluta de cada audio obtenido del servidor fravatel
						path_audios_4 = path_audios_3 + attr.filename
						#ruta absoluta del archivo que se guardara en nuestro servidor de aws
						path_local_2 = path_local + attr.filename
						#descarga el audio desde el servidor al cual nos conectamos a nuestro servidor en aws
						sftp.get(path_audios_4,path_local_2)
						#coloca un nombre referente al audio mp3
						nombre_audio = logica.asignar_nombre(attr.filename)
						#Llama a la funciòn que transforma archivo gsm y wav a mp3
						logica.transf_wav_a_mp3(path_local, path_local_2,nombre_audio)


		else:
			fecha_dia = str(int(n))
			path_audios_3 = path_audios_2 + '/' + fecha_dia + '/'
			#Cambiar a directorio remoto
			sftp.cwd(path_audios_3)
			#sftp.pwd-> indica la ruta absoluta del directorio
			# Obtener estructura del directorio
			lista = sftp.listdir_attr()
			#cantidad de elementos por carpeta(dia-> 01,02,03...31) del mes
			cont_archivos = len(lista)
			for attr in lista:
					#path_audios_4=path_audios_3 + attr.filename
					tam_arreglo = sftp.stat(attr.filename).st_size
					if tam_arreglo > 4000000:
						#ruta absoluta de cada audio obtenido del servidor fravatel
						path_audios_4 = path_audios_3 + attr.filename
						#ruta absoluta del archivo que se guardara en nuestro servidor de aws
						path_local_2 = path_local + attr.filename
						#descarga el audio desde el servidor al cual nos conectamos a nuestro servidor en aws
						sftp.get(path_audios_4,path_local_2)
						#coloca un nombre referente al audio mp3
						nombre_audio = logica.asignar_nombre(attr.filename)
						#Llama a la funciòn que transforma archivo gsm y wav a mp3
						logica.transf_wav_a_mp3(path_local, path_local_2,nombre_audio)
		
logica.contador(inicio_de_tiempo)		

	#sftp.exec_comand("pwd")

