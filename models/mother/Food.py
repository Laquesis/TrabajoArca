
import Animal from Animal.py
import Ark from Ark.py
class Food:
    #tipos de alimento
    #vegetal=0
    #animal = 1
    def _init_(self, name, tipo=None, cantidad=None):
        self.name=name
        self.tipo=tipo
        try:
            isinstance(cantidad , bool ) 
        except ValueError:
             raise "cantidad tiene que ser positivo"
        self.calorias=1
    
    def crear_alimento(self,name, tipo, calorias):
        self.name=name
        self.tipo=tipo
        self.calorias+=calorias

    def is_suitable(self, animal_type):
        #herbivoro =0
        #carnivoro=1
        #omnivoro=2
        suitable=False       
        match self.animal_type:
            case 0 :
                if self.tipo==0:
                    suitable=True
                else:
                    suitable=False              
            case 1:
                if self.tipo==0:
                    suitable=False
                else:
                    suitable=True
            case 2:
                suitable=True
            else:
                suitable=False
        
        return suitable
                


