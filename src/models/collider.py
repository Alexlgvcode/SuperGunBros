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
    def collides(app,collider1, collider2):
        
        if collider1 != collider2:
            left1 = collider1.position.x
            top1 = collider1.position.y
            left2 = collider2.position.x
            top2 = collider2.position.y
            right1 = collider1.position.x + collider2.width
            bottom1 = collider1.position.y + collider1.height
            right2 = collider2.position.x + collider2.width
            bottom2 = collider2.position.y + collider2.height
            if ((left1 <= right2) and (right1 >= left2) and (bottom1 >= top2)and (top1 <= bottom2)):
                print('Hit')
                app.floor = app.ground - collider2.height
            else:
                print('Not')
                app.floor = app.ground
                
            
                
            #if right1 >= left2 and right1 <= (left2+right2)//2:
                #collider1.position.x = collider2.position.x - collider1.width
                
            #if right2 >= left1 and left2:
               #collider1.position.x = right2

        


    @staticmethod
    def isCollision(app):
        #print(ColliderObstacle.collidersObstacle)
        for collider2 in ColliderObstacle.collidersObstacle:
            ColliderObstacle.collides(app,app.player.collider,collider2 )
                
                
    
    
    
    
    
    
    
   
    
                    

    
                    