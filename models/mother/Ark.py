from mother.Animal import Animal
from mother.Food import Food
class Ark:
    def __init__(self, animals=None, foods=None, water=None, max_capacity=None, left=False, tiempo=None):
        try:
            # Inicializar listas si no se pasan como argumentos
            if animals is None:
                animals = []
            if foods is None:
                foods = []
            if water is None:
                water = 0
            if tiempo is None:
                tiempo=0
            if max_capacity is None:
                max_capacity = {"animal": 100, "food": 1000, "water": 10000}

            # Verificación de tipos de datos
            if not isinstance(animals, list):
                raise TypeError("El atributo 'animals' debe ser una lista.")
            if not all(isinstance(animal, Animal) for animal in animals):
                raise TypeError("Todos los elementos de 'animals' deben ser instancias de la clase Animal.")

            if not isinstance(foods, list):
                raise TypeError("El atributo 'foods' debe ser una lista.")
            if not all(isinstance(food, Food) for food in foods):
                raise TypeError("Todos los elementos de 'foods' deben ser instancias de la clase Food.")
            if not isinstance(water, int):
                raise TypeError("El atributo 'water' debe ser un número entero.")
            if not isinstance(tiempo, int):
                raise TypeError("El atributo 'tiempo' debe ser un número entero.")
            if not isinstance(max_capacity, dict):
                raise TypeError("El atributo 'max_capacity' debe ser un diccionario.")
            if not isinstance(left, bool):
                raise TypeError("El atributo 'left' debe ser un valor booleano.")
            

            # Asignación a los atributos de la clase
            self.animals = animals
            self.foods = foods
            self.water = water
            self.max_capacity = max_capacity
            self.left = left
            self.tiempo=tiempo
        except TypeError as e:
            print(f"Error en la inicialización de Ark: {e}")

    def left_ark(self, left):
        try:
            if not isinstance(left, bool):
                raise TypeError("El parámetro 'left' debe ser un valor booleano.")
            if self.left==False:
                self.left=True
                self.tiempo +=1         
        except TypeError as e:
            print(f"Error en left_ark: {e}")

    def add_animal(self, animal):
        """Agregar un animal si hay capacidad disponible."""
        try:
            if len(self.animals) < self.max_capacity["animal"] and not self.left:
                self.animals.append(Animal(animal))
            else:
                print("No se pueden añadir más animales.")
        except KeyError as e:
            print(f"Error en add_animal: clave no encontrada en max_capacity: {e}")
        except Exception as e:
            print(f"Error en add_animal: {e}")

    def add_food(self, food):
        """Agregar comida si hay capacidad disponible."""
        try:
            if len(self.foods) < self.max_capacity["food"]:
                self.foods.append(Food(food))
            else:
                print("No se puede añadir más comida.")
        except KeyError as e:
            print(f"Error en add_food: clave no encontrada en max_capacity: {e}")
        except Exception as e:
            print(f"Error en add_food: {e}")

    def add_water(self, water):
        """Agregar agua si hay capacidad disponible."""
        try:
            if not isinstance(water, int):
                raise TypeError("El parámetro 'water' debe ser un número entero.")
            if self.water + water <= self.max_capacity["water"]:
                self.water += water
            else:
                print("No se puede añadir más agua.")
        except KeyError as e:
            print(f"Error en add_water: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_water: {e}")

    def add_multi_animal(self, list_animal):
        """Agregar múltiples animales si hay capacidad disponible."""
        try:
            if all(isinstance(animal, Animal) for animal in list_animal):
                raise TypeError("Todos los elementos de 'list_animal' deben ser instancias de la clase Animal.")
            if len(self.animals) + len(list_animal) <= self.max_capacity["animal"] and not self.left:
                self.animals.extend(list_animal)
            else:
                print("No se pueden añadir más animales.")        
        except KeyError as e:
            print(f"Error en add_multi_animal: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_multi_animal: {e}")

    def add_multi_food(self, list_food):
        """Agregar múltiples alimentos si hay capacidad disponible."""
        try:            
            if all(isinstance(food, Food) for food in list_food):
                raise TypeError("Todos los elementos de 'list_food' deben ser instancias de la clase Food.")
            if len(self.food) + len(list_food) <= self.max_capacity["food"]:
                self.food.extend(list_food)
            else:
                print("No se puede añadir más comida.")
        except KeyError as e:
            print(f"Error en add_multi_food: clave no encontrada en max_capacity: {e}")
        except TypeError as e:
            print(f"Error en add_multi_food: {e}")

    def get_status(self):
        """Mostrar el estado actual de la capacidad."""
        return {
            "animals": len(self.animals),
            "food": len(self.foods),
            "water": self.water,
            "max_capacity": self.max_capacity,
            "left": self.left
        }

    def search_list_suitable_food(food, animal_type):
        if not isinstance(food, Food):
            raise TypeError("El parámetro 'food' debe ser de la clase Food.")

        # Diccionario que asigna funciones lambda de validación según el tipo de animal
        is_suitable = {
            0: lambda f: f.tipo == 0,    # Herbívoro: solo acepta vegetal (tipo 0)
            1: lambda f: f.tipo == 1,    # Carnívoro: solo acepta carne (tipo 1)
            2: lambda _: True            # Omnívoro: acepta cualquier tipo de alimento
        }

        # Retorna True o False según si el alimento es adecuado
        return is_suitable.get(animal_type, lambda _: False)(food)
        
    def alimentar(self,animal):    
        if not animal.hunger:
            return self.foods  # Si el animal no tiene hambre, no consume nada
        if len(self.foods)<=0: # La lista no puede estar vacía           
            return self.foods

        calorias_necesarias = animal.size
        suitable_foods = [food for food in self.foods if Ark.search_list_suitable_food(food,Animal(animal).tipo)]

        for food in suitable_foods:
            if calorias_necesarias <= 0:
                break  # Se ha satisfecho la necesidad calórica
            if food.calorias <= calorias_necesarias:
                # Consume todo el alimento y resta sus calorías de la necesidad
                calorias_necesarias -= food.calorias
                self.foods.remove(food)
            else:
                # Consume solo una parte de las calorías del alimento y actualiza el alimento
                food.calorias -= calorias_necesarias
                calorias_necesarias = 0  # Se satisface la necesidad calórica
        
        if calorias_necesarias > 0:
            Animal(animal).hunger=True
            Animal(animal).life-=1
        else:
            Animal(animal).hunger=False
        
        self.tiempo+=1

        if self.tiempo==5:
            Ark.eliminar_caducados()
            self.tiempo=0      
  
    def beber(self,animal):
        if Animal(animal).thirst==True and self.water > 0:
            self.water-=(Animal(animal).size)
