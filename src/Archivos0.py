# Crear un archivo y escribir en el

archivo = open("../src/Archivos0.txt","a+")# w+ indica que se creara un archivo si este no existe o no lo encuentra. a lo concatena
archivo.write("Así se escribe en un fichero en Python")
archivo.read()
#archivo.close() #Se cierra el archivo
