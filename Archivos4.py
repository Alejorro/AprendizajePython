#escribir y leer concatenado a un archivo binario
import time

file = open("../src/Archivo4.dat", "a")

def escribir():
    palabra = input("Que desea escibir ")
    file.write("%s\n" % palabra)

def leer():
    file = open("../src/Archivo4.dat", "r")
    file.read()

escribir()
time.sleep(2)
leer()

print("Esto es una prueba de como hacerte una 'mejora' xD")