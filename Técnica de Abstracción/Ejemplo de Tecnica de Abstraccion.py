from abc import ABC, abstractmethod

# Clase abstracta
class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

# Clase concreta: Computadora
class Computadora(Dispositivo):
    def encender(self):
        return "La computadora está encendida."

    def apagar(self):
        return "La computadora está apagada."

# Clase concreta: Telefono
class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono está encendido."

    def apagar(self):
        return "El teléfono está apagado."

# Uso de las clases
def main():
    dispositivos = [Computadora(), Telefono()]
    for dispositivo in dispositivos:
        print(dispositivo.encender())
        print(dispositivo.apagar())

if __name__ == "__main__":
    main()