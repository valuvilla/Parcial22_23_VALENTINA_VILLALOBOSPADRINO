"""
a alianza rebelde necesita comunicarse de manera segura 
pero el imperio galáctico interviene todas la comunicaciones, 
por lo que la princesa Leia nos encarga el desarrollo de un algoritmo 
de encriptación para las comunicaciones rebeldes, que contemple los 
siguientes requerimientos:

 cada carácter deberá ser encriptado a ocho caracteres;
 se deberá generar dos tablas hash para encriptar y desencriptar, 
 para los caracteres desde el “ ” hasta el “}” -es decir desde el 
 32 al 125 de la tabla ASCII.
"""

# Encriptar y desencriptar con tablas hash
# Path: ej6.py
#


class nodoLista(object):
    """Clase nodoLista"""
    info, sig = None, None

class Lista(object):
    """Clase lista simplemente enlazada"""

    def __init__(self) -> None:
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

    def insertar(lista, dato):
        """Inserta el dato pasado en la lista"""
        nodo=nodoLista()
        nodo.info=dato
        if (lista.inicio == None) or (dato < lista.inicio.info):
            nodo.sig = lista.inicio
            lista.inicio = nodo

        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act != None) and (dato > act.info):
                ant= ant.sig
                act= act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamanio += 1

    def lista_vacia(lista):
        """Verifica si la lista está vacía"""
        return lista.inicio == None
        
    def eliminar(lista, clave):
        """Elimina un elemento de la lista y lo devuelve si lo encuentra"""
        if lista.inicio.info == clave:
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act != None) and (act.info != clave):
                ant = ant.sig
                act = act.sig
            if act != None:
                dato = act.info
                ant.sig = act.sig
                lista.tamanio -= 1
            else:
                raise Exception("No se encontró el dato")
        return dato
    
    def tamanio_lista(lista):
        """Devuelve el tamaño de la lista"""
        return lista.tamanio
    
    def buscar(lista, buscado):
        """Devuelve la dirección del elemento buscado"""
        aux=lista.inicio
        while (aux != None) and (aux.info != buscado):
            aux=aux.sig
        return aux
    
    def barrido(lista):
        """ Realiza un barrido de la lista"""
        aux=lista.inicio
        while aux != None:
            print(aux.info)
            aux=aux.sig

def crear_tabla_hash(tamanio):
    tabla=[None]*tamanio
    return tabla

def cantidad_elementos(tabla):
    return len(tabla)-tabla.count(None)


def funcion_hash(dato,tamanio_tabla):
    """Determina la posicion del dato en la tabla."""
    # hash por division para este caso
    return len(str(dato).strip())%tamanio_tabla

def agregar1(tabla, dato):
    """Agrega un elemento a la tabla encadenada."""
    posicion=funcion_hash(dato,len(tabla))
    if tabla[posicion] == None:
        tabla[posicion]=Lista()
    Lista.insertar(tabla[posicion],dato)


def encriptar(cadena,tabla):
    """Encripta una cadena de caracteres."""
    cadena_encriptada=""
    for i in range(len(cadena)):
        posicion=funcion_hash(ord(cadena[i]),len(tabla))
        if tabla[posicion] != None:
            cadena_encriptada+=str(tabla[posicion].inicio.info)
        else:
            cadena_encriptada+=cadena[i]
    return cadena_encriptada

def desencriptar(cadena,tabla):
    """Desencripta una cadena de caracteres."""
    cadena_desencriptada=""
    for i in range(len(cadena)):
        posicion=funcion_hash(ord(cadena[i]),len(tabla))
        if tabla[posicion] != None:
            cadena_desencriptada+=chr(tabla[posicion].inicio.info)
        else:
            cadena_desencriptada+=cadena[i]

if __name__=="__main__":
    encriptado=crear_tabla_hash(126)
    desencriptado=crear_tabla_hash(126)
    for i in range(32,126):
        agregar1(encriptado,i)
        agregar1(desencriptado,i)
    cadena="hola mundo"
    print("Cadena original: ",cadena)
    cadena_encriptada=encriptar(cadena,encriptado)
    print("Cadena encriptada: ",cadena_encriptada)
    cadena_desencriptada=desencriptar(cadena_encriptada,desencriptado)
    print("Cadena desencriptada: ",cadena_desencriptada)

    
#insertar, buscar, eliminar, lista_vacia