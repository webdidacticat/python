import os

print("El proceso actual (pid =% d) se está ejecutando ..."% (os.getpid()))
 # Escribir código en pycharm, el proceso padre del programa es pycharm;
print("El proceso padre del proceso actual es (pid =% d) se está ejecutando ..."% (os.getppid()))
print("Comenzar a crear proceso hijo ...")

pid = os.fork()
if pid == 0:
    #HIJO
         print("Esto es 0 devuelto por el proceso hijo, el pid del proceso hijo es% d, y el proceso padre es% d"%(os.getpid(), os.getppid()))
else:
    #PADRE
         print("Esto es devuelto por el proceso padre, el valor devuelto es el pid del proceso hijo, que es% d"%(pid))
