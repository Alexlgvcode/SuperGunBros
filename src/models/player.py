from models.gameObject import GameObject

class Player(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = True
    
    def jump(self, app):
        self.yVelocity = -app.jumpHeight
    
    def moveLeft(self):
        self.position.x -= 10
    
    def moveRight(self):
        self.position.x += 10  

    def applyGravity(self, app):
        if not (app.player.position.y + app.player.height >= app.floor):
            app.pressSpace = False
            self.isGrounded = False
            self.yVelocity += app.gravityInterval
            print('stop')
        elif not self.isGrounded:
            print(app.player.position.y)
            app.pressSpace = True
            self.yVelocity = 0
            self.isGrounded = True
           
            
    def setYVelocity(self):
        self.position.y += self.yVelocity
    