# Generar numeros aleatoreos que se guardaran en un fichero
import random

file = open("../src/Archivos2.txt","w+")

def numeroAleatoreo():
    for i in range(25):
        aleatoreo = random.randint(0,400)    
        file.write(str(aleatoreo))
        file.write("\n")

numeroAleatoreo()
file.close()