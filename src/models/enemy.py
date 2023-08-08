from models.gameObject import GameObject
class Enemy(GameObject):
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)