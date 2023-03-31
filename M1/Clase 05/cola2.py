class Jarra:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = 0

    def llenar(self):
        self.contenido = self.capacidad

    def vaciar(self):
        self.contenido = 0

    def verter_en(self, otra_jarra):
        espacio_disponible = otra_jarra.capacidad - otra_jarra.contenido
        cantidad_verter = min(self.contenido, espacio_disponible)

        self.contenido -= cantidad_verter
        otra_jarra.contenido += cantidad_verter


def main():
    jarra_5L = Jarra(5)
    jarra_3L = Jarra(3)

    while jarra_5L.contenido != 4:
        print("\nEstado actual:")
        print(f"Jarra de 5L: {jarra_5L.contenido} litros")
        print(f"Jarra de 3L: {jarra_3L.contenido} litros")

        print("\nOpciones:")
        print("1. Llenar la jarra de 3 litros")
        print("2. Llenar la jarra de 5 litros")
        print("3. Vaciar la jarra de 3 litros")
        print("4. Vaciar la jarra de 5 litros")
        print("5. Verter el contenido de la jarra de 3 litros en la de 5 litros")
        print("6. Verter el contenido de la jarra de 5 litros en la de 3 litros")

        opcion = int(input("Seleccione una opción (1-6): "))

        if opcion == 1:
            jarra_3L.llenar()
        elif opcion == 2:
            jarra_5L.llenar()
        elif opcion == 3:
            jarra_3L.vaciar()
        elif opcion == 4:
            jarra_5L.vaciar()
        elif opcion == 5:
            jarra_3L.verter_en(jarra_5L)
        elif opcion == 6:
            jarra_5L.verter_en(jarra_3L)
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 6.")

    print("\n¡Felicidades! Has logrado colocar 4 litros en la jarra de 5 litros.")

if __name__ == "__main__":
    main()
