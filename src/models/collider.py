from typing import List, Union, Tuple

class Collider:
    def __init__(self, position, height, width):
        self.position = position
        self.height = height
        self.width = width
        


class ColliderBullet:

    collidersBullet = []

    @staticmethod
    def collides(collider1, collider2):
     
        if collider1 != collider2:
            left0 = collider1.position.x
            top0 = collider1.position.y
            left1 = collider2.position.x
            top1 = collider2.position.y
            right0 = collider1.position.x + collider2.width
            bottom0 = collider1.position.y + collider1.height
            right1 = collider2.position.x + collider2.width
            bottom1 = collider2.position.y + collider2.height
            if ((right1 >= left0) and (right0 >= left1)
                and (bottom1 >= top0) and (bottom0 >= top1)):
                return True


    @staticmethod
    def isCollision():
        for collider1 in ColliderBullet.collidersBullet:
            for collider2 in ColliderBullet.collidersBullet:
                if ColliderBullet.collides(collider1, collider2):
                    return True
        return False
    
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
            #print(f'left1:{left1}  right1:{right1} top1:{top1} bottom1:{bottom1}/ left2:{left2}  right2:{right2} top2:{top2} bottom2:{bottom2}/')
    
            if ((left1 < right2 and left1> left2) or (right1 > left2 and right1 < right2)) and (top1 >= bottom2):
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
            #print(f'left1:{left1}  right1:{right1} top1:{top1} bottom1:{bottom1}/ left2:{left2}  right2:{right2} top2:{top2} bottom2:{bottom2}/')
           
            if ((3314 < left1 -app.scrollX<3415 ) or (4130 < left1 -app.scrollX < 4282 ))and top1 > bottom2:
                app.floor = app.height + 100
                return True
                
                
            if ((left1 < right2 and left1> left2) or (right1 > left2 and right1 < right2)) and (bottom1 < bottom2):
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
            #print(f'left1:{left1}  right1:{right1} top1:{top1} bottom1:{bottom1}/ left2:{left2}  right2:{right2} top2:{top2} bottom2:{bottom2}/')
        
            if (left1 <= right2 and left1>=left2) and (top1>=top2 and bottom1 <= bottom2):
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
            #print(f'left1:{left1}  right1:{right1} top1:{top1} bottom1:{bottom1}/ left2:{left2}  right2:{right2} top2:{top2} bottom2:{bottom2}/')
            
            if (right1 >= left2 and right1 <= right2) and (top1>=top2 and bottom1 <= bottom2):
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
        
        
                
                
    
    
    
    
    
    
    
   
    
                    

    
                    
                
    
    
    
    
    
    
    
   
    
                    

    
                    