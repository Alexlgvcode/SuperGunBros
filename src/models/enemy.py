from models.gameObject import GameObject
from models.vector import Vector2
from models.collider import ColliderEnemy
class Enemy(GameObject):
    
    def __init__(self, position, height, width, color):
        super().__init__(position, height, width, color)
       
    def enemies(app):
        enemies = [Enemy(Vector2(900+ app.scrollX,app.ground - 70), 70,70,'black')]
        ColliderEnemy.collidersEnemy = []
        for enemy in enemies:
            ColliderEnemy.collidersEnemy.append(enemy) 
        return enemies
    
    def enemyMoveRight(app):
        for enemy in Enemy.enemies(app):
            enemy.position.x +=5
            
    def enemyMoveLeft(app):
        for enemy in Enemy.enemies(app):
            enemy.position.x -=5