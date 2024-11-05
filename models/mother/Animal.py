class Animal:
    def __init__(self, name, hunger , thirst, type = None ) :
        self.name = name
        
        try : 
           isinstance(hunger , bool ) 
        except ValueError:
            raise "The hunger must be a positive number"
        try:
            isinstance(thirst , bool ) 
        except ValueError:
             raise "The thirst must be a positive number"
        self.hunger = hunger  # how much food does this animal eat when it is hungry
        self.thirst = thirst    # how much water does this animal drink when it is hungry
    
    #define a method to feed the animal
    def feed(self):
        if(self.hunger):
            self.hunger = False
        else:
            print(f"{self.name} is not hungary")
    def water(self):
        if(self.thirst):
            self.thirst = False
        else:
            print(f"{self.name} is not thirsty")


    def print_animal(self):
        print(self.name , self.type , self.hunger , self.thirst)


