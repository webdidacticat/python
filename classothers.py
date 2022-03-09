#!/usr/bin/env python3

###### init.py #############
import sys
import init2

class example:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello my name is " + self.name)


class example2: ## This is not work, it's wrong!!!
    def hello(self):
        print("Hello World, I'm example2")

if __name__ == "__main__":
    print("Hello World")
    sal = example("Pedro")
    sal.hello()
    #sal2 = example2
    #sal2.hello()
    if len(sys.argv) >= 2:
        print("Número de parámetros: ", len(sys.argv))
        print("Lista de argumentos: ", sys.argv)
        print("Segundo parametro: " + sys.argv[1])
    init2.saluda()

    
######## init2.py #############
def saluda():
    print("Hello World Init2")
