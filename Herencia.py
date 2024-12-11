class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def descripcion(self):
        return f"{super().descripcion()}, Carrera: {self.carrera}"

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def descripcion(self):
        return f"{super().descripcion()}, Materia: {self.materia}"

# Uso de las clases
def main():
    estudiante = Estudiante("Eduardo", 30, "Enfermeria")
    profesor = Profesor("Belen", 45, "Fisica")

    print(estudiante.descripcion())
    print(profesor.descripcion())

if __name__ == "__main__":
    main()