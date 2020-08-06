import pysftp
from pydub import AudioSegment
from datetime import date
import time

def transf_wav_a_mp3(filename_local,filename_sftp,renombre):

		#print("entro a la funcion")
	print(filename_local)
		#print(sftp.pwd)
	sound = AudioSegment.from_file(filename_sftp, format = "gsm")
	sound.export(filename_local + renombre + '.mp3', format = "mp3")



def asignar_nombre(nombre_antiguo):
	if nombre_antiguo[0] == 'q':
		
		ind_inicial_nombre = nombre_antiguo.find('9')
		ind_final_nombre = int(ind_inicial_nombre) + 18
		nombre_nuevo = nombre_antiguo[ind_inicial_nombre:ind_final_nombre]
	else:
		ind_inicial_nombre = nombre_antiguo.find('9')
		ind_final_nombre = int(ind_inicial_nombre) + 9
		nombre_nuevo = nombre_antiguo[ind_inicial_nombre:ind_final_nombre] + nombre_antiguo[14:23]
		print(nombre_nuevo)
	return nombre_nuevo


def contador(tiempo_inicial):
    tiempo_final = time.time() 
    tiempo_transcurrido = tiempo_final - tiempo_inicial
    print ('El proceso tomo ' + str(round(tiempo_transcurrido,2)) + ' segundos')



