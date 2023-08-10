from models.gameObject import GameObject
from models.collider import *

class Player(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = True
       
    
    def jump(self, app):
        self.yVelocity = -app.jumpHeight
    
    def moveLeft(self):
        self.position.x -= 8
    
    def sprintLeft(self):
        self.position.x -= 20
    def sprintRight(self):
        self.position.x += 20
        
    
    def moveRight(self):
        self.position.x += 8

    def playerWin(self,app):
        if self.position.x >= 626 and app.scrollX <= -8836 and not app.bossBattle:
            
            if app.player.position.x <= 930:
                Player.moveRight(self)
            elif app.player.position.x >=930:
                app.bossBattle = True
                app.bossBattleStart = True
            
        if app.bossBattleStart and app.player.position.x < 184:
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

