from models.gameObject import GameObject
from models.collider import *

class Player(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = True
        ColliderObstacle.collidersObstacle.append(self.collider)
    
    def jump(self, app):
        self.yVelocity = -app.jumpHeight
    
    def moveLeft(self):
        self.position.x -= 10
    
    def sprintLeft(self):
        self.position.x -= 20
    def sprintRight(self):
        self.position.x += 20
        
    
    def moveRight(self):
        self.position.x += 10  



    
    def applyGravity(self, app):
        if not (app.player.position.y + app.player.height >= app.floor):
            app.pressSpace = False
            self.isGrounded = False
            self.yVelocity += app.gravityInterval
        elif not self.isGrounded:
            app.pressSpace = True
            self.yVelocity = 0
            self.isGrounded = True
        
        
            
    def setYVelocity(self):
        self.position.y += self.yVelocity
    