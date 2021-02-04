'''
@autor: Jorge de la Rosa Padrón

Last update: 23/05/2020

'''

#LIBRERIAS
import random,sys							#Importamos las librerias necesarias, que son la de turtle para 					
from turtle import Screen, Turtle 		#poder dibujar y random para los numeros aleatorios
from tqdm import tqdm



################################  PARAMETROS PARA LA CONSTRUCCION DE LA IMAGEN  ###############################



#CONDICIONES INICIALES
pen    = Turtle()		      			#Le ponemos nombre a nuestra tortuga
screen = Screen()		 				#Esta condicion es necesaria para la grama cromatica en las hojas
random.seed()			  				#Inicializamos el generador de numeros aleatorios
screen.setup(800, 800)					#Definimos el tamaño de la pantalla
screen.colormode(255)					#Esta condicion es necesaria para poder pasarle a la gama cromatica los colores RGB
pen.speed(10)							#Velocidad de escritura (rango 0.5 - 10 donde 10 es el maximo) 				

count = 0

#DECLARACION DE FUNCIONES
#Funcion generador de terreno
def terreno(PROFUNDIDAD, DISTANCIA,one, two):
	pbar.update(1)	
	
	TURNSIDE = random.randint(0, 1) 	#Definimos aleatoriamente el lado de giro hacia el que va a girar, ya sea hacia arriba o hacia abajo
	ANGLE    = random.randint(one*0.8, two*0.8)	#Definimos el angulo de giro en el desarrollo del dibujo de la montaña

	if PROFUNDIDAD == 0:
		pen.forward(random.randint(int(DISTANCIA - (DISTANCIA/1.1)),int(DISTANCIA + (DISTANCIA/1.1)) )) 
		#^^Aquí pinta la distancia una vez dividida, entre los intervalos de distancia -^(distancia/1.2) y distancia + (distancia/1.2)
		#random.randint(a, b) nos devuelve un valor entero entre a y b
		
	else:
		DISTANCIA /= 2
		terreno(PROFUNDIDAD - 1, DISTANCIA,one, two)
		pen.left(ANGLE) if TURNSIDE == 0 else pen.right(ANGLE) #Esta condicion es para girar hacia arriba o hacia abajo
		terreno(PROFUNDIDAD - 1, DISTANCIA,one, two)
		pen.right(ANGLE) if TURNSIDE == 0 else pen.left(ANGLE) #Esta condicion es para girar hacia arriba o hacia abajo
		


#DECLARACION DE LAS VARIABLES PARA LA GENERACION DE LA MONTAÑA

DISTANCIA   = 1000 			#Los parametros que definen el terreno estan fijos porque no los he testeado lo suficiente
PROFUNDIDAD = 8
one = 5
two = 35



#CREACION DE LA MONTAÑA
TURNSIDE = random.randint(0, 1)  							#Definimos aleatoriamente ángulo inicial donde apuntará el puntero
ANGLE    = random.randint(10, 20)
pen.left(ANGLE) if TURNSIDE == 0 else pen.right(ANGLE)		#Decidir si apuntar hacia arriba o hacia abajo y con que angulo


pen.penup()													
pen.goto(-400,0)											
pen.pendown()	
with tqdm(total=511, file=sys.stdout) as pbar:
	terreno(PROFUNDIDAD, DISTANCIA,one, two)	#Funcion recursiva




#Presionar 'enter' para finalizar
input()

