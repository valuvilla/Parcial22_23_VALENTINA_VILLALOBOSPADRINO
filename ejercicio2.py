""""
Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y -1 si 145 no está en la lista
"""

def parte1(lista):
    laux=[] #creamos una lista auxiliar
    for i in range(0, len(lista)):
        if lista[i]%10==0 and lista[i]<200:
            laux.append(lista[i])
    return laux

def parte2(lista):
    #Para el programa si llega a un número mayor que 300
    laux=[] #creamos una lista auxiliar
    for i in range(0, len(lista)):
        if lista[i]>300:
            print(f"El numero {lista[i]} es mayor que 300")
            break
        else:
            laux.append(lista[i])
    return laux
            



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
    """Función auziliar para el merge sort"""
    lista_mezclada=[]
    while(len(izquierda) > 0 and len(derecha) > 0): #mientras la lista izquierda y la lista derecha tengan elementos
        if izquierda[0] < derecha[0]:
            lista_mezclada.append(izquierda.pop(0)) #agregamos el primer elemento de la lista izquierda a la lista mezclada
        else:
            lista_mezclada.append(derecha.pop(0)) #agregamos el primer elemento de la lista derecha a la lista mezclada
    if len(izquierda) > 0:
        lista_mezclada+=izquierda #agregamos los elementos restantes de la lista izquierda a la lista mezclada
    if len(derecha) > 0:
        lista_mezclada+=derecha #agregamos los elementos restantes de la lista derecha a la lista mezclada
    return lista_mezclada

def indice(lista, valor):
    """Función que devuelve el índice de un valor en una lista"""
    for i in range(0, len(lista)):
        if lista[i]==valor:
            return i
    return -1

if __name__ == "__main__":
    lista=[18, 50, 210, 80, 145, 333, 70, 30]
    print(f"Los numeros que cumplen esto son: {parte1(lista)}")
    print(f"Lista con los cambios: {parte2(lista)}")
    print(f'La lista ordenada es : {mergesort(lista)}')
    print(f'El número {145} se encuentra en la posicion : {indice(lista, 145)}')
