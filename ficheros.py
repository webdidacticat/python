# Abrir fichero de lectura : f = open("fichero.txt")
# Abrir fichero de lectura : f = open("fichero.txt", "r")
# Abrir fichero de lectura en binario : f = open("fichero.txt", "rb")
# Abrir fichero para escribir desde cero : f = open ("fichero.txt", "w")
# Abrir fichero para añadir al final : f = open ("fichero.txt", "a")
# Cerrar fichero: f.close()
# Lectura de todo el fichero de golpe: dato = f.read()
# Lectura de 100 bytes: dato = f.read(100)
# Lectura de una línea completa: dato = f.readline()
# Con f.tell() podemos saber en qué posición estamos del fichero y con f.seek()
# podemos desplazarnos por él, para leer o escribir en una determinada posición.
# f.seek(n): Ir al byte n del fichero
# f.seek(n, 0): Equivalente al anterior
# f.seek(n, 1): Desplazarnos n bytes a partir de la posición actual del fichero
# f.seek(n, 2): Situarnos n bytes antes del final de fichero.
# Modo de apertura----Descripción----Acción
# 'w'----Escritura----Si el fichero no existe lo crea. Si existe, borra su contenido
# 'r'----Lectura----Si existe fichero: lo abre. Si no existe: excepción FileNotFoundError
# 'a'----Añadir----Si fichero no existe, lo crea para escritura. Si existe, añade al final
# 'w+'----Actualizar----Escritura/ lectura. Si el fichero no existe lo crea. Si existe: borra
# 'r+'----Actualizar----Lectura/Escritura. Si no existe: excepción FileNotFoundError
# 'a+'----Añadir----Escritura/lectura. Si existe, añade al final.
# 'b'----Binario----Abre en binario. Combinadas con otras banderas: establece modo
# 'x'----Creación----Abre exclusivamente para crear fichero. Si ya existe, falla

def abrirfichero(name, sel):
    if sel:
        ## Creamos el fichero
        if len(name) == 0:
            print("Fichero por defecto")
            f = open("prueba.txt", "w")
            return f
        else:
            f = open(name, "w")
            return f
    else:
        ## Leemos el fichero
        if len(name) == 0:
            print("Fichero por defecto")
            f = open("prueba.txt", "r")
            return f
        else:
            f = open(name, "r")
            return f

def escribirfichero(f, msg):
    f.write(msg)

def leerfichero(f):
    dato = f.readline()
    print(dato)

def cerrarfichero(f):
    f.close()

namefile = input("Dime el nombre de un fichero")
f = abrirfichero(namefile, True)
escribirfichero(f, "Soy NOVATO, pero sigo siendo el REY")
cerrarfichero(f)
f = abrirfichero(namefile, False)
leerfichero(f)
cerrarfichero(f)
