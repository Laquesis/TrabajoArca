class Ark:
    def __init__(self, animals=None, foods=None,water=None, max_capacity=None, left=False):
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
        self.left=left
    
    def left_ark(self, left):
        self.left=True

    def add_animal(self, animal):
        """Agregar un animal si hay capacidad disponible."""
        if len(self.animal) < self.max_capacity["animal"]  and self.left=False:
            self.animals.append(animal)           
        else:
            print("No se pueden añadir más animales.")

    def add_food(self, food):
        """Agregar comida si hay capacidad disponible."""
        if len(self.food) < self.max_capacity["food"] :
            self.food.append(food)       
        else:
            print("No se puede añadir más comida.")

    def add_water(self, water):
        """Agregar agua si hay capacidad disponible."""
        if self.water < self.max_capacity["water"]:
            self.water +=water          
        else:
            print("No se puede añadir más agua.")

     def add_multi_animal(self, list_animal):
        """Agregar un animal si hay capacidad disponible."""
        if len(self.list_animal) < self.max_capacity["animal"]  and self.left=False:
            self.animals.extend(self.list_animal)           
        else:
            print("No se pueden añadir más animales.")

    def add_multi_food(self, list_food):
        """Agregar comida si hay capacidad disponible."""
        if len(self.list_food) < self.max_capacity["food"] :
            self.food.extend(self.list_food)       
        else:
            print("No se puede añadir más comida.")
  

    def get_status(self):
        """Mostrar el estado actual de la capacidad."""
        return {
            "animals": len(self.animals),
            "food": len(self.food),
            "water": self.water,
            "max_capacity": self.max_capacity,
            "left": self.left
        }
    def search_food(self,food):

