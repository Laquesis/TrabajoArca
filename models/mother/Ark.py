class Ark:
    def __init__(self, animals=None, foods=None,water=None max_capacity=None):
        # Inicializar listas si no se pasan como argumentos
        if animals is None:
            animals = []
        if foods is None:
            foods = []
        if water is None:
            water = 0
        if max_capacity is None:
            max_capacity = {"animal": 100, "food": 1000, "water": 10000}
        
        # Asignación a los atributos de la clase
        self.animals = animals
        self.food = foods
        self.water = water
        self.max_capacity = max_capacity

    def add_animal(self, animal):
        """Agregar un animal si hay capacidad disponible."""
        if len(self.animal) < self.max_capacity["animal"] :
            self.animals.append(animal)           
        else:
            print("No hay más capacidad para añadir animales.")

    def add_food(self, food):
        """Agregar comida si hay capacidad disponible."""
        if len(self.food) < self.max_capacity["food"]:
            self.food.append(food)       
        else:
            print("No hay más capacidad para añadir comida.")

    def add_water(self, water):
        """Agregar agua si hay capacidad disponible."""
        if self.water < self.max_capacity["water"]:
            self.water +=water          
        else:
            print("No hay más capacidad para añadir agua.")

    def get_status(self):
        """Mostrar el estado actual de la capacidad."""
        return {
            "animals": len(self.animals),
            "food": len(self.food),
            "water": self.water,
            "max_capacity": self.max_capacity
        }
