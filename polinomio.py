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

    def agregar_termino(polinomio, termino, valor):
        """Agrear un termino y si valo al polinomio"""
        aux=Nodo() #creamos un nodo auxiliar
        dato=datoPolinomio(valor, termino) #creamos un datoPolinomio
        aux.info=dato #le asignamos el datoPolinomio al nodo auxiliar
        if termino>polinomio.grado: #si el termino es mayor que el grado
            aux.sig=polinomio.termino_mayor #el nodo auxiliar apunta al termino mayor
            polinomio.termino_mayor=aux #el termino mayor apunta al nodo auxiliarp
            polinomio.grado=termino #el grado es igual al termino
        else:
            actual=polinomio.termino_mayor #creamos un nodo actual que apunta al termino mayor
            while actual.sig!=None and actual.sig.info.termino>termino: #mientras el nodo actual apunte a un nodo y el termino del nodo actual sea mayor que el termino
                actual=actual.sig #el nodo actual apunta al nodo siguiente
            aux.sig=actual.sig #el nodo auxiliar apunta al nodo actual
            actual.sig=aux #el nodo actual apunta al nodo auxiliar

    def modificar_termino(polinomio, termino, valor):
        """Modificar el valor de un termino del polinomio"""
        actual=polinomio.termino_mayor #creamos un nodo actual que apunta al termino mayor
        while actual!=None and actual.info.termino!=termino:
            actual=actual.sig
        actual.info.valor=valor

    def eliminar_termino(polinomio, termino):
        """Eliminar un termino del polinomio"""
        if polinomio.termino_mayor.info.termino==termino:
            polinomio.termino_mayor=polinomio.termino_mayor.sig
        else:
            aux=polinomio.termino_mayor #creamos un nodo auxiliar que apunta al termino mayor	
            while aux.sig!=None and aux.sig.info.termino!=termino:
                aux=aux.sig
            if aux.sig!=None and aux.sig.info.termino==termino:
                aux.sig=aux.sig.sig
            
    def obtener_valor(polinomio, termino):
        """Obtener el valor de un polinomio para un valor x"""
        aux=polinomio.termino_mayor #creamos un nodo auxiliar que apunta al termino mayor
        while aux!=None and aux.info.termino!=termino:
            aux=aux.sig
        if aux!=None and aux.info.termino==termino:
            return aux.info.valor
        else:
            return 0
        
    def mostrar_polinomio(polinomio):
        """Mostrar el polinomio"""
        aux=polinomio.termino_mayor #creamos un nodo auxiliar que apunta al termino mayor
        pol=""
        while aux!=None:
            signo="+" if aux.info.valor>=0 else ""
            pol=pol+signo+str(aux.info.valor)+"x^"+str(aux.info.termino)
            aux=aux.sig
        return pol
    
    def existe_polinomio(polinomio, termino):
        """Determinar si un termino existe en el polinomio"""
        aux=polinomio.termino_mayor #creamos un nodo auxiliar que apunta al termino mayor
        while aux!=None and aux.info.termino!=termino:
            aux=aux.sig
        if aux!=None and aux.info.termino==termino:
            return True
        else:
            return False
        
    def sumar(polinomio1,polinomio2):
        paux=Polinomio() #creamos un polinomio auxiliar
        mayor=polinomio1.grado if polinomio1.grado>polinomio2.grado else polinomio2.grado #determinamos el grado mayor
        for i in range(0,mayor+1):
            total=polinomio1.obtener_valor(i)+polinomio2.obtener_valor(i) #sumamos los valores de los polinomios
            if total != 0:
                paux.agregar_termino(i,total) #agregamos el termino al polinomio auxiliar
        return paux #retornamos el polinomio auxiliar
    
    def restar(polinomio1,polinomio2):
        paux=Polinomio() #creamos un polinomio auxiliar
        mayor=polinomio1.grado if polinomio1.grado>polinomio2.grado else polinomio2.grado #determinamos el grado mayor
        for i in range(0,mayor+1):
            total=polinomio1.obtener_valor(i)-polinomio2.obtener_valor(i)
            if total != 0:
                paux.agregar_termino(i,total)
        return paux
    
    def d

    