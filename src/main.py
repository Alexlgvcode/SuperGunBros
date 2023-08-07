from cmu_graphics import *
from models.obstacle import Obstacle
from models.player import Player
from models.vector import Vector2
from models.collider import *
from PIL import Image
import os, pathlib

### git add .
### git commit -m "(message)"
### git push

def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))


def onAppStart(app):
    app.keys = []
    app.releaseKeys = []
    
    
    app.width = 1280
    app.height = 720
    app.jumpHeight = 30
    app.stepsPerSecond = 70
    app.gravityInterval = 1
    app.stopMovementLeft = False
    app.stopMovementRight = False
    app.backgroundImage1 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap1.png')
    app.backgroundImage2 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap2.png')
    app.backgroundImage3 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap3.png')
    app.backgroundImage4 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap4.png')
    app.backgroundImage5 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap5.png')
    app.backgroundImage6 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap6.png')
    app.backgroundImage7 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap7.png')
    app.backgroundImage8 = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioMap8.png')
    
    spritestripright = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioRun2.png')
    spritestripLeft = Image.open('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioRunLeft2.png')
    app.sprites = []
    app.spritesLeft = []
    for i in range(3):
        sprite = CMUImage(spritestripright.crop((6+88*i, 6, 88+ 85 *i, 81)))
        app.sprites.append(sprite)
        spriteLeft = CMUImage(spritestripLeft.crop((6+88*i, 6, 88+ 85 *i, 81)))
        app.spritesLeft.append(spriteLeft)
    app.spriteCounter = 0

    
    
    app.backgroundX = 0
    
    restart(app)

        

def restart(app):
    app.paused = False
    app.gameOver = False
    app.gameStartScreen = True
    app.howToPlayScreen = False
    app.hoverStart = False
    app.hoverHowTo = False
    
    app.playerIdle = True
    app.playerRunRight = False
    app.playerRunLeft = False
    app.playerJump = False
    
    
    app.debug = False
    app.model = False
    app.scrollX = 0 


    
    app.falling = False
    app.floor = 623
    app.ground = 623
    app.maxHeight = 110
    app.ceiling = 0
    app.pressSpace = True
    
    
    
    
    player(app)
    obstacle(app)
    
    

def player(app):
    app.playerWidth  =  82
    app.playerHeight = 75
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
    if app.howToPlayScreen:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/SettingsPage.png',0,0) 
        
    elif app.gameStartScreen:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/GameStartScreen.png',0,0)
        if app.hoverHowTo:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/rulesHover.png',480,400)
        else:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/Rules.png',480,400)
        if app.hoverStart:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/StartButtonHover.png',520,500)
        else:
            drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/StartButton.png',520, 500)
    elif app.gameOver:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/GameOverScreen.png',0,0)
    
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
        drawLabel(f'x:{app.scrollX}', app.centerPlayerX, app.centerPlayerY -100, size = 20,fill = 'black')
        #app.scrollX = 0drawRect(50,app.ground-)


def drawBoard(app):
    #fontPath = '/Users/alexlgv/Documents/15-112/SuperGunBros/src/Fonts/Super Mario Bros. 2.ttf'
    #font = ImageFont.truetype(fontPath, size=30)
    if 0>= app.scrollX > -1296:
        drawImage(CMUImage(app.backgroundImage1),app.scrollX,0)
        drawImage(CMUImage(app.backgroundImage2),app.scrollX + app.width,0)
    elif -1296 >= app.scrollX > -2556:
        drawImage(CMUImage(app.backgroundImage2),app.scrollX+app.width ,0)
        drawImage(CMUImage(app.backgroundImage3),app.scrollX+app.width*2 ,0)
    elif -2556 >= app.scrollX > -3840:
        drawImage(CMUImage(app.backgroundImage3),app.scrollX+app.width*2 ,0)
        drawImage(CMUImage(app.backgroundImage4),app.scrollX+app.width*3 ,0)
    elif -3840>= app.scrollX > -5112:
        drawImage(CMUImage(app.backgroundImage4),app.scrollX+app.width*3 ,0)
        drawImage(CMUImage(app.backgroundImage5),app.scrollX+app.width*4 ,0)
    elif -5112>= app.scrollX >-6396:
        drawImage(CMUImage(app.backgroundImage5),app.scrollX+app.width*4 ,0)
        drawImage(CMUImage(app.backgroundImage6),app.scrollX+app.width*5 ,0)
    elif -6396 >= app.scrollX > -7548:
        drawImage(CMUImage(app.backgroundImage6),app.scrollX+app.width*5 ,0)
        drawImage(CMUImage(app.backgroundImage7),app.scrollX+app.width*6 ,0)
    elif -7548 >= app.scrollX >-8832:
        drawImage(CMUImage(app.backgroundImage6),app.scrollX+app.width*5 ,0)
        drawImage(CMUImage(app.backgroundImage7),app.scrollX+app.width*6 ,0)
        drawImage(CMUImage(app.backgroundImage8),app.scrollX+(app.width*7 - 128) ,0)
        
    elif -8820>= app.scrollX:
        drawImage(CMUImage(app.backgroundImage8),app.scrollX+(app.width*7 - 128) ,0)
    #drawLabel('Score:',50,50, font = font)

#------PLAYER CHARACTER--------
def drawPlayer(app):
    if app.playerRunRight:
        sprite = app.sprites[app.spriteCounter]
        drawImage(sprite,app.player.position.x, app.player.position.y)
    elif app.playerRunLeft:
        spriteLeft = app.spritesLeft[app.spriteCounter]
        drawImage(spriteLeft,app.player.position.x, app.player.position.y)
    elif app.playerIdle:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioIdle.png',app.player.position.x,app.player.position.y)
    elif app.playerJumpRight:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioJump.png',app.player.position.x, app.player.position.y)
    elif app.playerJumpLeft:
        drawImage('/Users/alexlgv/Documents/15-112/SuperGunBros/src/assets/MarioJumpLeft.png',app.player.position.x, app.player.position.y)
    #drawRect(app.player.position.x,app.player.position.y,app.player.width,app.player.height, fill = 'black')



def drawBlock(app):
    for obstacle in Obstacle.obstacles(app):
        drawRect(obstacle.position.x,obstacle.position.y, obstacle.width,obstacle.height, fill = obstacle.color, border = None)
    for collider in ColliderObstacle.collidersObstacle:
        drawRect(collider.position.x, collider.position.y, collider.width, collider.height, fill = None, border = 'red')
        #drawRect(ColliderObstacle.collidersObstacle[0].position.x, ColliderObstacle.collidersObstacle[0].position.y, ColliderObstacle.collidersObstacle[0].width, ColliderObstacle.collidersObstacle[0].height, fill = None, border = 'red')

def onKeyPress(app,key):
    if key == 'space':
        app.playerJumpRight = True
        app.playerIdle = False
        app.playerRunRight = False
        app.playerRunLeft = False
    if key == 'r':
        restart(app)
    if key == 'p':
        app.paused = not app.paused
    if key == 'l':
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
    app.keys = keys
    if not app.paused and not app.gameStartScreen:
        if 'space' in keys and app.pressSpace: 
            app.playerJump = True
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

                

            
            if 'd' in app.keys and not app.stopMovementRight and app.player.position.x + app.player.width< app.width:
                if 'space' not in app.keys:
                    app.playerRunRight = True
                    app.playerIdle = False
                if app.player.position.x < app.width//2 -100 or(app.scrollX <= -8832) :
                    app.player.moveRight()
                elif app.scrollX> -8832:
                    app.scrollX -= 20
                    
            
            elif 'a' in app.keys and app.player.position.x >0 and not app.stopMovementLeft:
                if app.scrollX <= 0 and app.scrollX >= -8832:
                    app.player.moveLeft()
                    if 'space' not in app.keys:
                        app.playerRunLeft = True
                        app.playerIdle = False
            if 'space' in app.keys and app.pressSpace: 
                
                if 'a' in app.keys:
                    app.playerJumpLeft = True
                    app.playerIdle = False
                    app.playerRunRight = False
                    app.playerRunLeft = False
                    
                elif 'd' in app.keys:
                        app.playerJumpRight = True
                        app.playerIdle = False
                        app.playerRunRight = False
                        app.playerRunLeft = False
                app.player.jump(app)
                    
            

            
        app.player.applyGravity(app)

        ColliderObstacle.isCollision(app)
def onKeyRelease(app,keys):
    if keys != 'space':
        app.keys.remove(keys)

def playerIdle(app):
    if app.keys == []:
        app.playerIdle = True
        app.playerRunRight = False
        app.playerRunLeft = False
        app.playerJump = False
        


    
def onMousePress(app,mouseX, mouseY):
    if 520 <= mouseX  <= 758 and 520 <= mouseY<= 604:
        app.gameStartScreen = False
    if 480 <= mouseX <=790 and 400 <= mouseY<= 465:
        app.howToPlayScreen = True
    if 500 <= mouseY <= 575 and 175 <= mouseX <= 250:
        app.howToPlayScreen = False
        

def onMouseMove(app,mouseX,mouseY):
    if 520 <= mouseX  <= 758 and 520 <= mouseY<= 604:
        app.hoverStart = True
    elif 480 <= mouseX <=790 and 400 <= mouseY<= 465:
        app.hoverHowTo = True
    else:
        app.hoverHowTo = False
        app.hoverStart = False
        
def onStep(app):    
    if not app.paused:

        print(app.keys, app.playerIdle)
        playerIdle(app)
        app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
        app.player.applyGravity(app)
        Obstacle.obstacles(app)
        app.player.setYVelocity()
        app.player.playerDeath(app)
        #app.block.outOfBounds(app)
    



runApp()