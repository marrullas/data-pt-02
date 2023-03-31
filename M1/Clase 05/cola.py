
"""
2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
Las opciones posibles son:
* Llenar la jarra de 3 litros
* Llenar la jarra de 5 litros
* Vaciar la jarra de 3 litros
* Vaciar la jarra de 5 litros
* Verter el contenido de la jarra de 3 litros en la de 5 litros
* Verter el contenido de la jarra de 5 litros en la de 3 litros
"""

class Cola:
    def __init__(self, max_lt=0):
        self.__list = []         # Inicializa la lista vacía
        self.__max_lt = max_lt   # Capacidad máxima en litros

    def llenar(self, item=None):
        if item:
            # Llena la cola con elementos mientras haya espacio y haya elementos disponibles
            while self.size() < self.__max_lt and item > 0:
                item -= 1
                self.__list.append(1)  # Añade elementos a la cola
            return item  # Retorna la cantidad de elementos que no se pudieron agregar
        else:
            self.__list = [1] * self.__max_lt  # Llena la cola completamente
            return self.size()  # Retorna la cantidad de elementos en la cola

    def vaciar(self):
        self.__list.clear()  # Vacia la lista

    def verter(self):
        cant = self.size()  # Guarda la cantidad de elementos en la cola
        self.vaciar()       # Vacía la cola
        return cant         # Retorna la cantidad de elementos que había en la cola

    def is_empty(self):
        return not bool(self.__list)  # Retorna True si la cola está vacía, False en caso contrario

    def size(self):
        return len(self.__list)  # Retorna la cantidad de elementos en la cola


def transferir(ori: Cola, dest: Cola):
    residuo = dest.llenar(ori.verter())  # Transfiere elementos de ori a dest
    if residuo > 0:  # Si no se pudieron transferir todos los elementos
        ori.llenar(residuo)  # Devuelve los elementos no transferidos a ori


if __name__ == '__main__':
    l5 = Cola(5)
    l3 = Cola(3)

    l3.llenar()
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    transferir(l3, l5)
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    l3.llenar()
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    transferir(l3, l5)
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    l5.vaciar()
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    transferir(l3, l5)
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    l3.llenar()
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    transferir(l3, l5)
    print(f'Cantidad L5: {l5.size()} Cantidad en L3: {l3.size()}')

    """
    5L      3l
    0       3
    3   <-  0
    3   <-  3
    5   ->  1
    0       1
    1   <-  0
    1   ->  3
    4   ->  0

    """