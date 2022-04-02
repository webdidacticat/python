#!/usr/bin/env python3

namefile = "dades"

def leer_fichero(): ### Abrimos para leer el fichero
    return open(namefile, "r")

def añadir_fichero(): ### Abrimos para añadir al final del fichero información
    return open(namefile, "a")

def crear_fichero(): ### Abrimos para crear y escribir el fichero información
    return open(namefile, "w")

def cerrar_fichero(f): ### Cerramos el fichero
    f.close

def fichero():
    ## Descubrimos si el fichero existe previamente
    try:
       f=leer_fichero()
    except:
       f=crear_fichero()
    cerrar_fichero(f)

if __name__ == "__main__":
    fichero()
