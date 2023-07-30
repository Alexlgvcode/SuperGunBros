from models.collider import Collider

class GameObject:
    def __init__(self, position, height, width, color):
        self.position = position
        self.height = height 
        self.width = width
        self.color = color
        self.collider = Collider(position, height, width)