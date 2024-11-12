# TrabajoArca
# Razieh GHAHARTARS
# Carmen RAMÍREZ
## Desafío: Creando el Arca de Noé con Clases de Python
## ENUNCIADO 
En este ejercicio, desarrollaremos un modelo de la famosa Arca de Noé utilizando programación orientada a objetos en Python. Crearemos una clase estática `Arca` que tendrá la capacidad de almacenar tanto animales como alimentos y agua. La arca tendrá contenedores específicos y finitos, y proporcionará métodos para gestionar los alimentos y cuidar de los animales, incluyendo alimentarlos y darles agua. 

### Parte 1: Crear la Clase Arca

1. Define una clase estática llamada `Arca` con los siguientes atributos y métodos:
   - **Atributos**:
     - `animales` (lista): Una lista para almacenar instancias de la clase `Animal`.
     - `alimentos` (lista): Una lista para almacenar instancias de la clase `Alimento`.
     - `agua` (int): Un contenedor que almacena la cantidad total de agua disponible.
     - `capacidad_maxima` (int): Un límite para la cantidad total de animales y alimentos que puede contener el arca.
   - **Métodos**:
     - `__init__(cls, capacidad_maxima)`: El método constructor que inicializa la capacidad máxima del arca y crea listas vacías para animales y alimentos, además de establecer el agua a un valor inicial.
     - `agregar_animal(cls, animal)`: Un método que agrega un objeto `Animal` a la lista de animales si no se supera la capacidad máxima.
     - `agregar_alimento(cls, alimento)`: Un método que agrega un objeto `Alimento` a la lista de alimentos.
     - `agregar_agua(cls, cantidad)`: Un método que agrega agua al contenedor de agua.
     - `alimentar_animal(cls, animal)`: Un método que proporciona alimento a un animal específico.
     - `dar_agua(cls, animal)`: Un método que proporciona agua a un animal específico.
     - `estado_arca(cls)`: Un método estático que devuelve el estado actual de la arca, como el número de animales, alimentos y la cantidad de agua almacenados.

### Parte 2: Crear las Clases Padre Animal y Alimento

2. Define una clase llamada `Animal` con los siguientes atributos y métodos:
   - **Atributos**:
     - `nombre` (str): El nombre del animal.
     - `tipo` (str): El tipo de animal (por ejemplo, "perro", "gato").
     - `hambre` (int): Un nivel que indica cuánta hambre tiene el animal.
     - `sed` (int): Un nivel que indica cuánta sed tiene el animal.
   - **Métodos**:
     - `__init__(self, nombre, tipo)`: El método constructor que inicializa el nombre y tipo del animal, y establece hambre y sed a un valor inicial.
     - `alimentar(self)`: Un método que reduce el nivel de hambre del animal.
     - `dar_agua(self)`: Un método que reduce el nivel de sed del animal.
     - `estado(self)`: Un método que devuelve el estado actual de hambre y sed del animal.

3. Define una clase llamada `Alimento` con los siguientes atributos y métodos:
   - **Atributos**:
     - `tipo` (str): El tipo de alimento (por ejemplo, "heno", "croquetas").
     - `cantidad` (int): La cantidad de alimento disponible.
   - **Métodos**:
     - `__init__(self, tipo, cantidad)`: El método constructor que inicializa el tipo de alimento y la cantidad.
     - `usar(self, cantidad)`: Un método que reduce la cantidad de alimento disponible en la cantidad especificada.
     - `es_alimento_adecuado(cls, tipo_animal)`: Un método estático que verifica si un tipo de alimento es adecuado para un tipo de animal dado.

### Parte 3: Crear Clases Derivadas

4. Crea clases derivadas de `Animal` para diferentes tipos de animales (por ejemplo, `Perro`, `Gato`) que pueden tener métodos específicos o atributos adicionales.

5. Crea clases derivadas de `Alimento` para diferentes tipos de alimentos (por ejemplo, `Heno`, `Croquetas`) que pueden tener métodos específicos o atributos adicionales.

### Parte 4: Usando las Clases

6. Crea una instancia de la clase `Arca` con una capacidad máxima definida.

7. Crea instancias de los animales y alimentos derivados de sus respectivas clases padre.

8. Añade los animales y alimentos creados a la instancia de `Arca`.

9. Añade agua al contenedor de agua usando el método `agregar_agua`.

10. Simula el proceso de alimentar a los animales y darles agua utilizando los métodos correspondientes de la clase `Arca`.

11. Utiliza el método estático `estado_arca` para verificar el estado actual del arca.

### Desafíos Adicionales (Opcional, solo si tienes tiempo):

12. Implementa manejo de errores en tus clases para asegurar que no se puedan agregar más animales o alimentos que la capacidad máxima de la arca.

13. Crea un método para mostrar el estado de todos los animales en el arca, incluyendo su nombre, tipo, hambre y sed.

Este ejercicio te ayudará a comprender cómo usar la programación orientada a objetos para modelar un sistema más complejo, además de permitirte practicar la creación de jerarquías de clases y la interacción entre ellas. La inclusión de métodos estáticos también te dará experiencia en la implementación de funcionalidad que no depende del estado específico de una instancia.

# ENLACES DEL PROYECTO
## CLICK UP
https://app.clickup.com/t/8696kpmqq

## Repositorios
# Principal
https://github.com/Laquesis/TrabajoArca
# Django
https://github.com/Laquesis/djangoArcaNoe

## Diagrama de clases
https://miro.com/welcomeonboard/MzR4SDRIVEhXYTBQWHZPOTJDZWNNY0pyRXNvOHhXb1BqNTB6YVFRQ1VFSGtWSU1vd0JHRnNwc2Q1enlkOTBOQlFOQW4vRGZ3ZnBiNmJHRmtxNWlHTjBQa3JFajV1d0lmbDM1WGhncGN6Zmg3TktoN21SL2lsNkQ3ZFhOSzdxUEshZQ==?share_link_id=706057329282






