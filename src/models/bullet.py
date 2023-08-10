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
            jumpVelocity = 10
            bullet.yVelocity = -jumpVelocity
        
    def moveBullets(app):
        #Bullet follows the line that goes from the player until the mouse 
        if app.powerUp:
            bulletRate = 10
            for bullet in Bullet.bullets:
                bullet.position.y += bulletRate * bullet.slope
                bullet.position.x += bulletRate
        else:
            bulletRate = 5
            for bullet in Bullet.bullets:

                bullet.position.x += bulletRate
                bullet.position.y += bullet.yVelocity
                Bullet.applyGravity(app, bullet)
        if app.bossBattle:
            Bullet.moveBowserAttack(app)
    
    def moveBowserAttack(app):
        #Bowser's attack follows the player until it reaches it and then goes straight
        trackingLimit = 300
        bulletRate = 10
        for attack in app.bowserAttacks:  
            if attack.position.x > app.player.position.x + trackingLimit:
                attack.slope = ((attack.position.y - app.player.position.y)/ 
                                (attack.position.x-app.player.position.x))
            attack.position.y -= bulletRate * attack.slope
            attack.position.x -= bulletRate
            
    def applyGravity( app,bullet):    
        if not (bullet.position.y + bullet.height >= app.bulletFloor):
                bullet.isGrounded = False
                bullet.yVelocity += app.gravityInterval
                
        elif not bullet.isGrounded:
            bullet.isGrounded = True
            bullet.position.y = app.bulletFloor - bullet.height
            bullet.yVelocity = 0
            Bullet.jump(bullet)
            
            
    
    def setYVelocity(bullet):
        bullet.position.y += bullet.yVelocity

                

            
