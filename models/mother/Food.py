class Food:
    
    def _init_(self, tipo=None, cantidad=None):
        self.tipo=tipo
        try:
            isinstance(cantidad , bool ) 
        except ValueError:
             raise "cantidad tiene que ser positivo"
        self.cantidad=0
    
    def crear_alimento(self,tipo, cantidad):

