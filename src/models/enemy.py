from models.gameObject import GameObject
from models.vector import Vector2
from models.collider import ColliderEnemy

class Enemy(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
        self.startingX =self.position.x
        self.moveLeft = True
        
    def load(app):
        enemies = app.enemies
        ColliderEnemy.collidersEnemy = []
        for enemy in enemies:
            ColliderEnemy.collidersEnemy.append(enemy) 
        
    
    
    
    def moveRight(enemy):
        movingRate = 4
        enemy.startingX += movingRate
            
    def moveLeft(enemy):
        movingRate = 4
        enemy.startingX -= movingRate
    def slideLeft(self):
        slidingRate = 12
        self.position.x -= slidingRate
    def moveDown(enemy):
        rocketSpeed = 10
        enemy.position.y+= rocketSpeed
            
    def outOfBounds(app):
        for enemy in app.enemies:
            if enemy.position.x <=  -enemy.width:
                app.enemies.remove(enemy)
                ColliderEnemy.collidersEnemy.remove(enemy)