from cmu_graphics import *
from models.obstacle import Obstacle
from models.player import Player
from models.vector import Vector2
from models.collider import *
### git add .
### git commit -m "(message)"
### git push




def onAppStart(app):
        app.width = 1280
        app.height = 720
        app.jumpHeight = 10
        app.stepsPerSecond = 70
        app.gravityInterval = 0.8
        
        
        restart(app)
    
        

def restart(app):
    app.debug = False
    
    
    app.floor = 623
    app.ground = 623
    app.maxHeight = 110
    app.ceiling = app.ground - app.maxHeight
    app.pressSpace = True
    app.paused = False
    
    player(app)
    obstacle(app)
    

def player(app):
    app.playerWidth  = 40
    app.playerHeight = 40
    app.playerY = app.floor - app.playerHeight
    app.playerX = app.width//3
    app.playerRight = app.playerX + app.playerWidth
    app.playerBottom = app.playerY + app.playerHeight
    app.centerPlayerX = (app.playerRight +app.playerX) //2
    app.centerPlayerY = (app.playerBottom +app.playerY) //2
    app.playerColor = 'blue'
    app.player = Player(Vector2(app.playerX,app.playerY), app.playerHeight,app.playerWidth, app.playerColor)

def obstacle(app):
    app.blockWidth = 40
    app.blockHeight = 40
    app.blockX  = app.width
    app.blockY = app.ground - app.blockHeight
    app.blockRight = app.blockX + app.blockWidth
    app.blockBottom = app.blockY + app.blockHeight
    app.blockColor = 'green'
    app.block = Obstacle(Vector2(app.blockX, app.blockY),app.blockHeight, app.blockWidth, app.blockColor)
    

    
def redrawAll(app): 
    drawBoard(app)
    drawPlayer(app)
    drawBlock(app)
    debug(app)
    
    
def debug(app):
    if app.debug:
        drawLine(0,app.floor,app.width,app.floor)
       

def drawBoard(app):
    drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap.jpeg', 0, 0)
    #drawImage('/Users/alexlgv/Documents/15-112/TermProject/minecraftHill.png', 0 ,0)
    #drawRect(0,0,app.width,app.height, fill = 'lightblue')
    #drawRect(0,app.ground, app.width ,app.height, fill = 'black')
    #drawLine(0,app.ceiling, app.width, app.ceiling)




#------PLAYER CHARACTER--------
def drawPlayer(app):
    #drawRect(app.playerX, app.playerY, app.playerWidth,
             #app.playerHeight, fill = 'blue', border = app.playerColor)
    drawImage('/Users/alexlgv/Documents/15-112/TermProject/GeometryDashPlayer.png',app.player.position.x,app.player.position.y)
    
def drawBlock(app):
    for obstacle in Obstacle.obstacles:
        
        drawRect(obstacle.position.x,obstacle.position.y, obstacle.width,obstacle.height, fill = obstacle.color, border = 'black')
        

def onKeyPress(app,key):
    if key == 'r':
        restart(app)
    if key == 'p':
        app.paused = not app.paused
    if key == 'd':
        app.debug = not app.debug
        
def onKeyHold(app, keys):
    if 'space' in keys and app.pressSpace: 
        app.player.jump(app)
    if 'right' in keys:
        app.player.moveRight()
    if 'left' in keys:
        app.player.moveLeft()
        


        
def onStep(app):
    #print(app.player.position.y)
    if not app.paused:
        Obstacle.moveObstacle()
        app.block.generateObstacles(app)
        app.player.applyGravity(app)
        app.player.setYVelocity()
        app.block.outOfBounds(app)

        if ColliderManager.isCollision():
            print('Game Over')
        
        
    
runApp()
