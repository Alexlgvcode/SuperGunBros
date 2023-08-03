from models.vector import Vector2
from models.gameObject import GameObject
from models.collider import *

import random


class Obstacle(GameObject):
    
    
    
    
        
    def __init__(self, position, height, width, color):
        super().__init__(position, height,width, color)
    
    def obstacles(app):
        obstacles = [Obstacle(Vector2(1350+ app.scrollX, app.ground - 90),100, 90, app.blockColor),
                     Obstacle(Vector2(960 + app.scrollX, app.ground - 190),50, 240, app.blockColor),
                     Obstacle(Vector2(1830 + app.scrollX, app.ground - 145),150, 90, app.blockColor),
                     Obstacle(Vector2(2220 + app.scrollX, app.ground - 187),187, 80, app.blockColor),
                     Obstacle(Vector2(2745 + app.scrollX, app.ground - 187),187, 82, app.blockColor)
                     ]
        ColliderObstacle.collidersObstacle = []
        for i in range(len(obstacles)):
            ColliderObstacle.collidersObstacle.append(obstacles[i].collider)
        return obstacles

        
    
    @staticmethod
    def outOfBounds(app):
        for obstacle in Obstacle.obstacles(app):
            if obstacle.position.x <=  -app.blockWidth:
                Obstacle.obstacles(app).remove(obstacle)
                ColliderObstacle.collidersObstacle.remove((obstacle.collider))


    def obstacleGenerator(self,app):
        self.height = random.randint(app.blockHeight, 400 )
        self.position.y -= self.height
        self.position.x = app.width//2
        
    def __repr__(self):
        return f'{Obstacle.obstacles}'
        