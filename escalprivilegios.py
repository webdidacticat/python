#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comprobar si el usuario es root
"""

import os
import subprocess

euid = os.geteuid()
#print(euid)
if os.geteuid() != 0:
    print('Debes tener privilegios root para este script.')
    dades = subprocess.run(['pkexec', 'dirección de donde se encuntra el programa que necesita privilegios',variables que son necesarias para el programa], stdout=subprocess.PIPE,shell=False)
    if dades.returncode != 0:
        print("ERROR")
        exit(0)

if os.geteuid() == 0:
    print('Tenemos sudo privilegios!!!')
else:
    print('No tenemos privilegios')
