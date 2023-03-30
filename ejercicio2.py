""""
Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y -1 si 145 no está en la lista
"""


def mergesort(lista):
    """"Método de ordenamiento mergesort"""
    if len(lista) <= 1:
        return lista
    else:
        medio=len(lista)//2 #dividimos la lista en dos
        izquierda=[] #creamos una lista izquierda
        for i in range(0, medio):
            izquierda.append(lista[i]) #agregamos los elementos de la lista a la lista izquierda
        derecha=[] #creamos una lista derecha
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda=mergesort(izquierda) #llamamos recursivamente al método mergesort para la lista izquierda
        derecha=mergesort(derecha) #llamamos recursivamente al método mergesort para la lista derecha
        if (izquierda[medio-1] <= derecha[0]): 
            izquierda+=derecha #si el último elemento de la lista izquierda es menor o igual al primer elemento de la lista derecha
            return izquierda #retornamos la lista izquierda
        else:
            return merge(izquierda, derecha)
        

def merge(izquierda, derecha):
    