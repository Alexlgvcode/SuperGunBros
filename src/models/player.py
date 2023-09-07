from models.gameObject import GameObject
from models.collider import *

class Player(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = True
        self.speed = 8
       
    
    def jump(self, app):
        self.yVelocity = -app.jumpHeight
    
    def moveLeft(self):
        self.position.x -= self.speed
    
        
    
    def moveRight(self):
        self.position.x += self.speed

    def playerWin(self,app):
        flagPosition = 626
        scrollingIndex = -8836
        if (self.position.x >= flagPosition and 
            app.scrollX <= -scrollingIndex and 
            not app.bossBattle):
            
            castlePosition = 930
            if app.player.position.x <= castlePosition:
                Player.moveRight(self)
            elif app.player.position.x >= castlePosition:
                app.bossBattle = True
                app.bossBattleStart = True
        startingPosition = 184
        if app.bossBattleStart and app.player.position.x < startingPosition:
            Player.moveRight(self)
        
            

    
    def playerDeath(self,app):
        if self.position.y >= app.height or app.timeLeft <= 0 :
            app.gameOver = True
    
    def applyGravity(self, app):
        
        if not (app.player.position.y + app.player.height >= app.floor):
            app.pressSpace = False
            self.isGrounded = False
            self.yVelocity += app.gravityInterval
        
        elif not self.isGrounded:
            self.isGrounded = True
            app.playerIdle = True
            app.playerRunRight = False
            app.playerRunLeft = False
            app.playerJump = False
            app.falling = False
            app.player.position.y = app.floor-app.player.height
            app.pressSpace = True

            self.yVelocity = 0
            
            
    def setYVelocity(self):
        self.position.y += self.yVelocity

