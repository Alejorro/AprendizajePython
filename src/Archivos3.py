#crear un array de strings y guardarlo en un fichero
import array
file = open("Archivos3.txt", "w")

def crearArray():
    coleccion = ["Alfa Romeo","Ferrari","Masseratti", "Lamborghini", "Bugatti"]

    for item in coleccion:
        file.write("%s\n" % item)
        
    
    file.close()

crearArray()