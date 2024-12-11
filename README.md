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


Explico el codigo Herencia
Clase Base Persona
Contiene un constructor que inicializa nombre y edad.
Tiene un método descripcion que devuelve información básica sobre la persona.
Clases Derivadas Estudiante y Profesor
Ambas heredan de Persona.
Cada clase tiene su propio constructor que llama al constructor de la clase base usando super(), añadiendo información específica carrera para Estudiante y materia para Profesor.
Sobrescriben el método descripcion para incluir la información adicional.
Uso de las Clases
En la función main, se crean instancias de Estudiante y Profesor.
Se imprime la descripción de cada uno


Explico el codigo Polimorfismo
Clase Base Empleado
Es un método presentar, que se espera que sea implementado por las subclases. Si no se implementa, se lanza un error.
Clases Derivadas Desarrollador y Gerente
Ambas heredan de Empleado.
Implementamos el método presentar de manera diferente
Desarrollador Devuelve el mensaje "Hola, soy un desarrollador."
Gerente Devuelve el mensaje "Hola, soy un gerente."
Uso de las Clases
En la función main, se crean instancias de Desarrollador y Gerente.


