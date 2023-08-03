from models.gameObject import GameObject
from models.collider import *

class Player(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = True
        #ColliderObstacle.collidersObstacle.append(self.collider)
    
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
        if app.player.position.y < app.ceiling:
            app.falling = True
            app.player.position.y = app.ceiling
            
        if app.falling:
            app.pressSpace = False
            self.isGrounded = False
            self.yVelocity += app.gravityInterval
        if not (app.player.position.y + app.player.height >= app.floor):
            app.pressSpace = False
            self.isGrounded = False
            self.yVelocity += app.gravityInterval
        
        elif not self.isGrounded:
            self.isGrounded = True
            app.falling = False
            app.player.position.y = app.floor-app.player.height
            app.pressSpace = True
            self.yVelocity = 0
            
            
        
        
            
    def setYVelocity(self):
        self.position.y += self.yVelocity
    