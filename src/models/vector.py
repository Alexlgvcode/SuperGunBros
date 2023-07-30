
class Vector2:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self,other)-> bool:
        return(isinstance(other, type(self)) and self.x == other.x and self.y == other.y)
    


   
    


        
    
        

    