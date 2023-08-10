from models.gameObject import GameObject
from models.collider import ColliderBullet

class Bullet(GameObject):
    bullets = []
    
    def __init__(self, position, height,width,slope,person,color):
        super().__init__(position, height, width, color)
        self.yVelocity = 0
        self.isGrounded = False
        if person == 'player':
            ColliderBullet.collidersBulletObstacle.append(self)
            Bullet.bullets.append(self)
        self.slope = slope
        
    
        
    def jump(bullet):
            bullet.yVelocity = -10
        
    def moveBullets(app):
        if app.powerUp:
             for bullet in Bullet.bullets:
                bullet.position.y += 10 * bullet.slope
                bullet.position.x += 10
        else:
            for bullet in Bullet.bullets:

                bullet.position.x += 5
                bullet.position.y += bullet.yVelocity
                Bullet.applyGravity(app, bullet)
        if app.bossBattle:
            Bullet.moveBowserAttack(app)
    
    def moveBowserAttack(app):
        for attack in app.bowserAttacks:  
            if attack.position.x > app.player.position.x + 300:
                attack.slope = ((attack.position.y - app.player.position.y)/ (attack.position.x-app.player.position.x))
            attack.position.y -= 10* attack.slope
            attack.position.x -= 10 
            
    def applyGravity( app,bullet):    
        if not (bullet.position.y + bullet.height >= app.bulletFloor):
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

                

            
