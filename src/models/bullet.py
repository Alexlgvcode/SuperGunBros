from models.gameObject import GameObject
from models.collider import ColliderBullet

class Bullet(GameObject):
    bullets = []
    
    def __init__(self, position, height,width,color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = False
        ColliderBullet.collidersBulletObstacle.append(self)
        Bullet.bullets.append(self)
    
        
    def jump(bullet):
            bullet.yVelocity = -10
        
    def moveBullets(app):
        for i in range(len(Bullet.bullets)):

            Bullet.bullets[i].position.x += 5
            Bullet.bullets[i].position.y += Bullet.bullets[i].yVelocity
            Bullet.applyGravity(app,Bullet.bullets[i])
            
    def applyGravity( app,bullet):    
        if not ( bullet.position.y + bullet.height >= app.bulletFloor):
                #print(bullet.position.x, bullet.position.y, bullet.isGrounded)
                bullet.isGrounded = False
                bullet.yVelocity += app.gravityInterval
                
        elif not bullet.isGrounded:
            bullet.isGrounded = True
            bullet.position.y = app.bulletFloor - bullet.height
            bullet.yVelocity = 0
            Bullet.jump(bullet)
            
            
    
    def setYVelocity(bullet):
        bullet.position.y += bullet.yVelocity

                

            
