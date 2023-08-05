from models.vector import Vector2
from models.gameObject import GameObject
from models.collider import *

import random


class Obstacle(GameObject):
    
    
    
    
        
    def __init__(self, position, height, width, color):
        super().__init__(position, height,width, color)
    
    def obstacles(app):
        
        obstacles = [Obstacle(Vector2(770+ app.scrollX, app.ground - 190),50, 50, app.blockColor),
                     
                     Obstacle(Vector2(1350+ app.scrollX, app.ground - 90),100, 90, app.blockColor),
                     Obstacle(Vector2(960 + app.scrollX, app.ground - 190),50, 240, app.blockColor),
                     Obstacle(Vector2(1830 + app.scrollX, app.ground - 145),150, 90, app.blockColor),
                     Obstacle(Vector2(2216 + app.scrollX, app.ground - 187),187, 80, app.blockColor),
                     Obstacle(Vector2(2738 + app.scrollX, app.ground - 187),187, 82, app.blockColor),
                     Obstacle(Vector2(3250 + app.scrollX, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(3405 + app.scrollX, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(3690+ app.scrollX, app.ground - 190),50, 145, app.blockColor),
                     Obstacle(Vector2(3830+ app.scrollX, app.ground - 385),50, 380, app.blockColor),
                     Obstacle(Vector2(4060+ app.scrollX, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(4260 + app.scrollX, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(4355 + app.scrollX, app.ground - 385),50, 195, app.blockColor),
                     Obstacle(Vector2(4786 + app.scrollX,app.ground-193), 50,100, app.blockColor),
                     Obstacle(Vector2(5655 + app.scrollX,app.ground-193), 50,50, app.blockColor),
                     Obstacle(Vector2(5800 + app.scrollX,app.ground-381), 50,145, app.blockColor),
                     Obstacle(Vector2(6135 + app.scrollX,app.ground-381), 50,195, app.blockColor),
                    
                     Obstacle(Vector2(6425 + app.scrollX,app.ground-50), 50,50, app.blockColor),
                     Obstacle(Vector2(6470 + app.scrollX,app.ground-95), 50,50, app.blockColor),
                     Obstacle(Vector2(6520 + app.scrollX,app.ground-140), 50,50, app.blockColor),
                     Obstacle(Vector2(6565 + app.scrollX,app.ground-190), 200,50, app.blockColor),
                     
                     Obstacle(Vector2(6710 + app.scrollX,app.ground-190), 200,50, app.blockColor),
                     Obstacle(Vector2(6760 + app.scrollX,app.ground-140), 50,50, app.blockColor),
                     Obstacle(Vector2(6810 + app.scrollX,app.ground-95), 50,50, app.blockColor),
                     Obstacle(Vector2(6860 + app.scrollX,app.ground-50), 50,50, app.blockColor),
                     
                     Obstacle(Vector2(7100 + app.scrollX,app.ground-50), 50,45, app.blockColor),
                     Obstacle(Vector2(7148 + app.scrollX,app.ground-95), 50,45, app.blockColor),
                     Obstacle(Vector2(7195 + app.scrollX,app.ground-140), 50,45, app.blockColor),
                     Obstacle(Vector2(7245 + app.scrollX,app.ground-190), 200,45, app.blockColor),
                     Obstacle(Vector2(7290 + app.scrollX,app.ground-190), 200,45, app.blockColor),
                     
                     
                     Obstacle(Vector2(8690+ app.scrollX, app.ground -50),50, 400, app.blockColor),
                     
                     
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
        