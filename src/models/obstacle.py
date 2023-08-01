from models.vector import Vector2
from models.gameObject import GameObject
from models.collider import *
import random


class Obstacle(GameObject):

    obstacles =  []
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height,width, color)
        Obstacle.obstacles.append(self)
        ColliderObstacle.collidersObstacle.append(self.collider)

        
    @staticmethod
    def generateObstacles(app):
        #obstacleHeight = random.randint(app.blockHeight, 200)
        
        if Obstacle.obstacles[-1].position.x + app.blockWidth< app.width and app.count >= 120:
            Obstacle(Vector2(app.width, app.ground-app.blockHeight), app.blockHeight,app.blockWidth,app.blockColor)
            
            app.count = 0
        
   
                 
      
    @staticmethod
    def moveObstacle():
        for obstacle in Obstacle.obstacles:
                obstacle.position.x -= 5
    
    @staticmethod
    def outOfBounds(app):
        for obstacle in Obstacle.obstacles:
            
            if obstacle.position.x <=  -app.blockWidth:
                Obstacle.obstacles.remove(obstacle)
                ColliderObstacle.collidersObstacle.remove((obstacle.collider))


    def obstacleGenerator(self,app):
        self.height = random.randint(app.blockHeight, 400 )
        self.position.y -= self.height
        self.position.x = app.width + self.width
        
    def __repr__(self):
        return f'{Obstacle.obstacles}'
        