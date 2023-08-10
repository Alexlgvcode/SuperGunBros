from models.gameObject import GameObject
from models.vector import Vector2
from models.collider import ColliderEnemy
import random

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
        enemy.startingX += 4
            
    def moveLeft(enemy):
        enemy.startingX -= 4
    def slideLeft(self):
        self.position.x -= 12
    def moveDown(enemy):
        enemy.position.y+= 10
            
    def outOfBounds(app):
        for enemy in app.enemies:
            if enemy.position.x <=  -enemy.width:
                app.enemies.remove(enemy)
                ColliderEnemy.collidersEnemy.remove(enemy)