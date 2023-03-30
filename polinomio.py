# clase Polinomio
import unittest
from colorama import Fore, Back, Style
from termcolor import colored
"""
Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
•  restar;
•  dividir;
•  eliminar un término;
•  determinar si un término existe en un polinomio.
"""

#Creamos clase nodo
class Nodo(object):
    """clase nodo simplemente enlazado"""
    info, sig = None, None

class datoPolinomio(object):
    """Clase dato Polinomio"""
    def __init__(self, valor, termino):
        self.valor = valor #coeficiente
        self.termino = termino #exponente

class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crear un polinomio de grado 0"""
        self.termino_mayor=None
        self.grado=-1

    def agregar_termino(poil)
    