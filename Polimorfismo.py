class Empleado:
    def presentar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Desarrollador(Empleado):
    def presentar(self):
        return "Hola, soy un desarrollador."

class Gerente(Empleado):
    def presentar(self):
        return "Hola, soy un gerente."

# Uso de las clases
def main():
    empleados = [
        Desarrollador(),
        Gerente()
    ]

    for empleado in empleados:
        print(empleado.presentar())

if __name__ == "__main__":
    main()