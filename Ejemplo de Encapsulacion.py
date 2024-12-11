class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # Método para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para obtener la edad
    def obtener_edad(self):
        return self.__edad

    # Método para establecer la edad
    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")


# Uso de la clase
def main():
    persona = Persona("Ana", 30)

    print(f"Nombre: {persona.obtener_nombre()}")
    print(f"Edad: {persona.obtener_edad()}")

    # Cambiando la edad
    persona.establecer_edad(35)
    print(f"Nueva edad: {persona.obtener_edad()}")

    # Intentando establecer una edad negativa
    persona.establecer_edad(-5)


if __name__ == "__main__":
    main()