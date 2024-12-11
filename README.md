# Tarea-de-POO
Ejemplos de Técnicas de programación Abstracción, Encapsulación, Herencia, Polimorfismo
Explico el codigo de abstraccion
Clase Abstracta Dispositivo, define dos métodos abstractos, encender y apagar que deben ser implementados por cualquier clase que herede de Dispositivo.

Clases Concretas Computadora y Teléfono, implementan los métodos encender y apagar, proporcionando la lógica específica para cada tipo de dispositivo.

La Función main, crea una lista de dispositivos y muestra el resultado de encender y apagar cada uno.


Explico el codigo encapsulacion
Los atributos privados atributos __nombre y __edad son privados, lo que significa que no pueden ser accedidos directamente desde fuera de la clase.
Métodos Públicos La clase proporciona métodos públicos
obtener_nombre y obtener_edad para acceder a los atributos privados.
y establecer_edad para modificar la edad, con una validación para asegurarse de que la edad no sea negativa.
Uso de la Clase En la función main, se crea una instancia de Persona se obtienen y muestran el nombre y la edad se cambia la edad y se intenta establecer una edad negativa.


Explico el codigo Polimorfismo
crearemos una clase base llamada Empleado y dos clases derivadas Desarrollador y Gerente. Cada clase implementará un método presentar, demostrando el polimorfismo.
