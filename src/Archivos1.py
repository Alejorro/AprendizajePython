#Leer el archivo generado en Archivos0.py

file = open("../src/Archivos0.txt", "r")

def leerArchivo():
    print (file.read())

leerArchivo()