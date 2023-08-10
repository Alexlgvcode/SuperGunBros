

class Collider:
    def __init__(self, position, height, width):
        self.position = position
        self.height = height
        self.width = width
class ColliderEnemy:
    collidersEnemy =[] 
    
    def collides(collider1,collider2):
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider2.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
            if ((right2 >= left1) and (right1>= left2) and 
                (bottom2>top1) and (bottom1 >= top2)):
                return True
        
    def collidesLeft(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
           
        
            if ((left1 <= right2 and left1>=left2) and 
                (top1>=top2 and bottom1 <= bottom2)):
                return True


    def collidesRight(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
            
            
            if ((right1 >= left2 and right1 <= right2) and 
                (top1>=top2 and bottom1 <= bottom2)):
                return True
            
    
    def isCollision(app):

        for collider2 in ColliderEnemy.collidersEnemy:  
            if ColliderEnemy.collides(app.player.collider, collider2):
                app.gameOver =True
                break
        if not app.bossBattle:
            for collider1 in ColliderBullet.collidersBulletObstacle:
                for collider2 in ColliderEnemy.collidersEnemy:  
                    if ColliderEnemy.collides(collider1, collider2):
                        ColliderEnemy.collidersEnemy.remove(collider2)
                        ColliderBullet.collidersBulletObstacle.remove(collider1)
                        app.bulletRemove = collider1
                        app.enemies.remove(collider2)
                        app.score +=50

                        return True
        elif app.bossBattle:
            for collider1 in ColliderBullet.collidersBulletObstacle:
                if ColliderEnemy.collides(collider1, app.bowser):
                    app.bulletRemove =collider1
                    ColliderBullet.collidersBulletObstacle.remove(collider1)
                    app.bowserLife -= 20
                    return True
            for attack in app.bowserAttacks:
                if ColliderEnemy.collides(attack, app.player):
                    app.gameOver = True
                    break
                    
        for collider1 in app.rockets:
            if ColliderEnemy.collides(app.player.collider,collider1):
                app.gameOver = True
                break
            
        for collider1 in app.shells:
            if ColliderEnemy.collides(app.player.collider,collider1):
                app.gameOver= True
                break
            
        
        
    
                
                
                    
                    
        
            

        
class ColliderBullet:

    collidersBulletObstacle = []
    

    @staticmethod
    def collidesBot(app,collider1, collider2):
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider2.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
            if (((left1 < right2 and left1> left2) or
                (right1 > left2 and right1 < right2)) and 
                (bottom1 < bottom2)):
                app.bulletFloor = collider2.position.y
                return True
            else:
                app.bulletFloor = app.ground
                
            
    def collidesSide(collider1, collider2):
     
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider2.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
            if (((left1 < right2 and left1> left2) or 
                (right1 > left2 and right1 < right2)) and 
                (bottom1 < bottom2 and top1>=top2)):
                return True

                    

    @staticmethod
    def isCollisionObstacle(app):
        
        for collider1 in ColliderObstacle.collidersObstacle:
            for collider2 in ColliderBullet.collidersBulletObstacle:
                if ColliderBullet.collidesBot(app,collider1, collider2):
                    
                    break
        for collider1 in ColliderBullet.collidersBulletObstacle:
            for collider2 in ColliderObstacle.collidersObstacle:
                if ColliderBullet.collidesSide(collider1, collider2):
                    ColliderBullet.collidersBulletObstacle.remove(collider1)
                    app.bulletRemove = collider1
                    return True
        
                    
        
                    

    

    
class ColliderObstacle:

    collidersObstacle = []
    @staticmethod
    def collidesTop(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
        
    
            if (((left1 < right2 and left1> left2) or 
                (right1 > left2 and right1 < right2)) and 
                (top1 >= bottom2)):
                app.ceiling = bottom2+2
                return True 
            else:
                app.ceiling = -50
                
    def collidesBot(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
           
            if (((3258 < left1 -app.scrollX and right1-app.scrollX<3400 ) or 
                (4130 < left1 -app.scrollX and right1-app.scrollX < 4260 )or 
                (7335<left1 - app.scrollX and right1-app.scrollX < 7433))and 
                (top1 > bottom2)):
                app.floor = app.height + 100
                return True
                
                
            if (((left1 < right2 and left1> left2) or (
                right1 > left2 and right1 < right2))
                and (bottom1 < bottom2)):
                app.floor = collider2.position.y 
                return True
    
            else:
                app.floor = app.ground
                
    def collidesLeft(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
        
            if ((left1 <= right2 and left1>=left2) and 
                (top1>=top2 and bottom1 <= bottom2)):
                app.player.position.x = right2 
                app.stopMovementLeft = True
                return True
            return False

    def collidesRight(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider1.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
           
            
            if ((right1 >= left2 and right1 <= right2) and 
                (top1>=top2 and bottom1 <= bottom2)):
                app.player.position.x = left2-app.player.width 
                app.stopMovementRight = True
                return True
                
            return False


    @staticmethod
    def isCollision(app):
        #print(ColliderObstacle.collidersObstacle)
        
        for collider2 in ColliderObstacle.collidersObstacle:
            
                
            if ColliderObstacle.collidesTop(app,app.player.collider, collider2):
                break
            
        for collider2 in ColliderObstacle.collidersObstacle:
            if ColliderObstacle.collidesBot(app,app.player.collider,collider2 ):
                break
          
        for collider2 in ColliderObstacle.collidersObstacle:
            if ColliderObstacle.collidesLeft(app,app.player.collider,collider2 ):
                break
            else:
                app.stopMovementLeft = False
                
        for collider2 in ColliderObstacle.collidersObstacle:   
            if ColliderObstacle.collidesRight(app,app.player.collider,collider2 ):
                break
            else:
                app.stopMovementRight = False
        
        
                
                
    
    
    
    
    
    
    
   
    
                    

    
                    
                
    
    
    
    
    
    
    
   
    
                    

    
                    