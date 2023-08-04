from cmu_graphics import *
from models.obstacle import Obstacle
from models.player import Player
from models.vector import Vector2
from models.collider import *
from PIL import Image

### git add .
### git commit -m "(message)"
### git push




def onAppStart(app):
        app.width = 1280
        app.height = 720
        app.jumpHeight = 30
        app.stepsPerSecond = 70
        app.gravityInterval = 1
        app.stopMovementLeft = False
        app.stopMovementRight = False
        app.backgroundImage = Image.open('assets/MarioFullMap.png')
        app.backgroundX = 0
        
        restart(app)
    
        

def restart(app):
    app.debug = False
    app.model = False
    app.count = 0
    app.scrollX = 0 
    app.gameStartScreen = True
    app.hover = False

    
    app.falling = False
    app.floor = 623
    app.ground = 623
    app.maxHeight = 110
    app.ceiling = 0
    app.pressSpace = True
    app.paused = False
    
    
    
    player(app)
    obstacle(app)
    
    

def player(app):
    app.playerWidth  =  40
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
    app.blockWidth = 120
    app.blockHeight = 40
    app.blockX  = app.width
    app.blockY = app.ground - app.blockHeight
    app.blockRight = app.blockX + app.blockWidth
    app.blockBottom = app.blockY + app.blockHeight
    app.blockColor = None
    
    app.block = Obstacle(Vector2(app.blockX, app.blockY),app.blockHeight, app.blockWidth, app.blockColor)
    

    
def redrawAll(app): 
    if app.gameStartScreen:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/GameStartScreen.png',0,0)
        if app.hover:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/StartButtonHover.png',520,500)
        else:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/StartButton.png',520, 500)
    else:
        drawBoard(app)
        drawPlayer(app)
        drawBlock(app)
    
    debug(app)
    
    
def debug(app):
    if app.debug:
        drawLine(0,app.floor,app.width,app.floor, fill = 'red')
        drawLine(0,app.ground,app.width,app.ground, fill = 'blue')
        drawLine(0, app.ceiling,app.width,app.ceiling,fill = 'yellow')
        for i in range(0, app.height,50):
            drawLine(0,i,app.width,i)
            drawLabel(f'{i}', 20, i+20)
        for i in range(0,app.width,50):
            drawLine(i,0,i,app.height)
            drawLabel(f'{i}', i +20, 20)
        drawLabel(f'x:{app.player.position.x}, y: {app.player.position.y}', app.centerPlayerX , app.centerPlayerY- 40, size = 12,fill = 'white')
        drawLabel(f'x:{Obstacle.obstacles(app)[0].position.x}, y:{Obstacle.obstacles(app)[0].position.y}',Obstacle.obstacles(app)[0].position.x,Obstacle.obstacles(app)[0].position.y - 40, size = 12, fill = 'white')
        drawLabel(f'x:{app.scrollX}', app.centerPlayerX, app.centerPlayerY -100, size = 20,fill = 'white')
        #app.scrollX = 0drawRect(50,app.ground-)


def drawBoard(app):
    drawImage(CMUImage(app.backgroundImage),app.scrollX,0)
    #drawImage('/Users/alexlgv/Documents/15-112/TermProject/minecraftHill.png', 0 ,0)
    #drawRect(0,0,app.width,app.height, fill = 'lightblue')
    #drawRect(0,app.ground, app.width ,app.height, fill = 'black')
    #drawLine(0,app.ceiling, app.width, app.ceiling)


#------PLAYER CHARACTER--------
def drawPlayer(app):
   
    drawRect(app.player.position.x,app.player.position.y,app.player.width,app.player.height, fill = 'black')



def drawBlock(app):
    for obstacle in Obstacle.obstacles(app):
        drawRect(obstacle.position.x,obstacle.position.y, obstacle.width,obstacle.height, fill = obstacle.color, border = None)
    for collider in ColliderObstacle.collidersObstacle:
        drawRect(collider.position.x, collider.position.y, collider.width, collider.height, fill = None, border = 'red')
        #drawRect(ColliderObstacle.collidersObstacle[0].position.x, ColliderObstacle.collidersObstacle[0].position.y, ColliderObstacle.collidersObstacle[0].width, ColliderObstacle.collidersObstacle[0].height, fill = None, border = 'red')

def onKeyPress(app,key):
    if key == 'r':
        restart(app)
    if key == 'p':
        app.paused = not app.paused
    if key == 'd':
        app.debug = not app.debug
    if key == 't':
        app.model = not app.model
        if not app.model:
            app.playerWidth  = 40
            app.playerHeight = 40
        else:
            app.player.width =  52
            app.player.height = 55
        
def onKeyHold(app, keys):
    if not app.paused and not app.gameStartScreen:
        if 'space' in keys and app.pressSpace: 
            app.player.jump(app)
        if 's'in keys:
            if 'left' in keys and app.player.position.x>0 :
                if app.scrollX< 0:
                    app.scrollX += 20
                else:
                    app.player.sprintLeft()
                    
            if 'right'in keys and not app.stopMovementRight :
                if app.scrollX< 0:
                    app.scrollX -= 20
                else:
                    app.player.sprintRight()
                    
        else:      
            if 'right' in keys and not app.stopMovementRight:
                if app.player.position.x < app.width//3 or app.scrollX<= -8856:
                    app.player.moveRight()
                elif app.scrollX> -8856:
                    app.scrollX -= 12
                    
            
            if 'left' in keys and app.player.position.x >0 and not app.stopMovementLeft:
                if app.scrollX < 0 and app.scrollX >= -8856:
                    app.scrollX += 12
                else:
                    app.player.moveLeft()
        app.player.applyGravity(app)
        ColliderObstacle.isCollision(app)
    
def onMousePress(app,mouseX, mouseY):
    if 520 < mouseX  < 758 and 520 < mouseY< 604:
        app.gameStartScreen = False
        
def onMouseMove(app,mouseX,mouseY):
    if 520 <= mouseX  <= 758 and 520 <= mouseY<= 604:
        app.hover = True
    else: 
        app.hover = False
    

    
    
#def wall(app):
    #if ColliderObstacle.isCollision():
        #app.player.position.x = 
        
def onStep(app):
    print(app.scrollX)
    #print(app.player.position.y)
    if not app.paused:
        app.count +=1
        app.player.applyGravity(app)
        
        Obstacle.obstacles(app)
        app.player.setYVelocity()
        #app.block.outOfBounds(app)
        
            
            
        
        #app.player.updateFloor(app)
        #if ColliderObstacle.isCollision():
            #print('Game Over')
        

runApp()
