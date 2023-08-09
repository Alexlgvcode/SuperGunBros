from models.vector import Vector2
from models.gameObject import GameObject
from models.collider import *


import random


class Obstacle(GameObject):
    def __init__(self, position, height, width, color):
        super().__init__(position, height,width, color)
        self.startingX = self.position.x
    
    def obstacle(app):
        obstacles = app.obstacles
        ColliderObstacle.collidersObstacle = []
        for i in range(len(obstacles)):
            ColliderObstacle.collidersObstacle.append(obstacles[i].collider)
        
        return obstacles

        
    
    @staticmethod
    def outOfBounds(app):
        for obstacle in app.obstacles:
            if obstacle.position.x <=  -app.blockWidth:
                app.obstacles.remove(obstacle)
                ColliderObstacle.collidersObstacle.remove((obstacle.collider))


    def obstacleGenerator(self,app):
        self.height = random.randint(app.blockHeight, 400 )
        self.position.y -= self.height
        self.position.x = app.width//2
        
    def __repr__(self):
        return f'{self.position.x}'
        