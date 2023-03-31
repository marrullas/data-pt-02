
"""
1) Implementar un juego, que consista en apilar números enteros del 1 al 20, de forma aleatoria, para lo cual debe usarse una estructura de Pila. 
Luego, el usuario debe elegir un número de veces en que se va a quitar elementos de la pila, los cuales, sumados entre sí, no deben superar el valor de 50.
El usuario pierde si la suma supera ese valor. Si no lo supera, gana, pero su calificación será 10 menos el número elementos que falten quitar para todavía no superar 50.
El programa debe informar si perdió, y si ganó, con qué calificación lo hizo.

Consideraciones:<br>
a. Se puede usar la función input() para obtener una entrada de teclado.<br>
b. Se puede usar la el modulo random para obtener valores aleatorios.
"""

import random

class Ruleta_Pila(object):
    def __init__(self):
        self.__list = []
        self.cargar()
        #self.sacar(numero)

    # Agregar un elemento a la Pila
    def push(self, item):
        self.__list.append(item)
        return 'Ha ingresado el elemento: ',item
    # Quitar un elemento de la Pila ... PRESTEN ATENCIÓN
    def pop(self):
        return 'Se eliminó el elemento: ',self.__list.pop()
    # Obtener el elemento superior de la Pila
    def peek(self):
        if self.__list:
            #return 'El ultimo elemento de la lista es: ', self.__list[-1]
            return self.__list[-1]
        else:
            return 'No hay nada en la lista'
    # Determinar si la Pila está vacía
    def is_empty(self):
        if self.__list == []:
            return 'La lista está vacía'
        else:
            return 'La lista tiene los siguientes elementos', self.__list
    # Devuelve el número de elementos de la lista:
    def size(self, show_data = False):
        longitud = len(self.__list)
        if(show_data):
            return longitud
        return {f'La lista contiene: {longitud} elementos'}
    #cargar los 20 numeros aleatorios
    def cargar(self):
        i=0
        while i < 20:
            i += 1
            self.push(random.randint(0,20))
    #sacar un numero X de valores de la pila
    def tirar(self, numero):
        i=0
        resultado = 0
        llegar_50 = 0
        numeros_salida = []
        while i < self.size(True):
            i += 1
            #numeros_salida.append(self.peek())
            if(i < numero):
                resultado += self.peek()
                llegar_50 += self.peek()
            #else:

            self.pop()
        return {f'La suma de los valores que saco de la pila es {resultado}'}

if __name__ == '__main__':
    s = Ruleta_Pila()
    print(s.tirar(4))