from models.vector import Vector2
from models.gameObject import GameObject
from models.collider import *
import random

class Obstacle(GameObject):

    obstacles =  []
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height,width, color)
        Obstacle.obstacles.append(self)
        ColliderManager.colliders.append(self.collider)
        
    @staticmethod
    def generateObstacles(app):
        #obstacleHeight = random.randint(app.blockHeight, 200)
        if Obstacle.obstacles[-1].position.x + app.blockWidth + 300< app.width:
            Obstacle(Vector2(app.width, app.ground-app.blockHeight), app.blockWidth,app.blockHeight,app.blockColor)
        
        
      
    @staticmethod
    def moveObstacle():
        for obstacle in Obstacle.obstacles:
                obstacle.position.x -= 10
    
    @staticmethod
    def outOfBounds(app):
        for obstacle in Obstacle.obstacles:
            if obstacle.position.x <=  -app.blockWidth:
                Obstacle.obstacles.remove(obstacle)
                ColliderManager.colliders.remove((obstacle.collider))


    def obstacleGenerator(self,app):
        self.height = random.randint(app.blockHeight, 400 )
        self.position.y -= self.height
        self.position.x = app.width + self.width
        
    def __repr__(self):
        return f'{Obstacle.obstacles}'
        