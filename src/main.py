from cmu_graphics import *
from models.obstacle import Obstacle
from models.player import Player
from models.vector import Vector2
from models.collider import *
from models.bullet import *
from models.enemy import *
import random
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
    app.stepsPerSecond = 50
    app.gravityInterval = 2
    app.stopMovementLeft = False
    app.stopMovementRight = False
    app.backgroundImage1 = Image.open('assets/MarioMap1.png')
    app.backgroundImage2 = Image.open('assets/MarioMap2.png')
    app.backgroundImage3 = Image.open('assets/MarioMap3.png')
    app.backgroundImage4 = Image.open('assets/MarioMap4.png')
    app.backgroundImage5 = Image.open('assets/MarioMap5.png')
    app.backgroundImage6 = Image.open('assets/MarioMap6.png')
    app.backgroundImage7 = Image.open('assets/MarioMap7.png')
    app.backgroundImage8 = Image.open('assets/MarioMap8.png')
    app.marioBossMap = Image.open('assets/MarioBossMap.png')
    app.Fireball = Image.open('assets/Fireball.png')
    app.rocket = Image.open('assets/Rocket.png')
    app.shell = Image.open('assets/Shell.png')
    app.bowserImage = Image.open('assets/Bowser.png')
    app.bottomImage = Image.open('assets/BottomMap.png')
    app.bowserTitle = Image.open('assets/bowserTitle.png')
    
    
    spritestripright = Image.open('assets/MarioRun2.png')
    spritestripLeft = Image.open('assets/MarioRunLeft2.png')
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
    app.ticks = 0
    app.paused = True
    app.gameOver = False
    app.gameWon = False
    
    
    app.timerShell =100
    app.timerRocket = 300
    app.bossBattle = False
    app.bossBattleStart = False
    app.gameStartScreen = True
    app.howToPlayScreen = False
    app.pauseScreen = False
    app.gameWonScreen =False
    app.hoverStart = False
    app.hoverHowTo = False

    
    app.powerUp = False
    app.bulletRemove = None

    app.enemyRemove = None
    app.enemyRunLeft = True
    app.enemyRunRight = False
    
    app.bullet = None
    app.playerHide = False
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
    app.bulletFloor = 623
    app.maxHeight = 110
    app.ceiling = 0
    app.pressSpace = True
    
    app.score = 0
    app.timeLeft = 400
    
    player(app)
    obstacle(app)
    rocket(app)
    #Enemy positions determined by hand, overlapping the hardCoded map.
    app.enemies = [Enemy(Vector2(900,app.ground - 70), 70,70,'black'),
                   Enemy(Vector2(1000,app.ground - 70), 70,70,'black'),
                   Enemy(Vector2(2656,app.ground - 70), 70,70,'black'),
                    Enemy(Vector2(6343,app.ground - 70), 70,70,'black'),
                    Enemy(Vector2(8420,app.ground - 70), 70,70,'black'),
                    Enemy(Vector2(8504,app.ground - 70), 70,70,'black'),
                   ]
    
    
    app.rockets = []
    
    app.shells =[]
    
    app.bowserAttacks = []
    
    #Obstacle positions determined by hand, overlapping the hardCoded map.
    app.obstacles = [
                     
                     Obstacle(Vector2(1350, app.ground - 90),100, 90, app.blockColor),
                     Obstacle(Vector2(960 , app.ground - 190),50, 240, app.blockColor),
                     Obstacle(Vector2(1830 , app.ground - 145),150, 90, app.blockColor),
                     Obstacle(Vector2(2216 , app.ground - 187),187, 80, app.blockColor),
                     Obstacle(Vector2(2738 , app.ground - 187),187, 82, app.blockColor),
                     Obstacle(Vector2(3200 , app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(3400 , app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(3645, app.ground - 190),50, 180, app.blockColor),
                     Obstacle(Vector2(3830, app.ground - 385),50, 380, app.blockColor),
                     Obstacle(Vector2(4060, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(4260, app.ground),200, 50, app.blockColor),
                     Obstacle(Vector2(4355 , app.ground - 385),50, 195, app.blockColor),
                     Obstacle(Vector2(4786 ,app.ground-193), 50,140, app.blockColor),
                     Obstacle(Vector2(5605,app.ground-193), 50,100, app.blockColor),
                     Obstacle(Vector2(5800 ,app.ground-381), 50,145, app.blockColor),
                     Obstacle(Vector2(6135 ,app.ground-381), 50,195, app.blockColor),
                     Obstacle(Vector2(6425,app.ground-100), 100,90, app.blockColor),
                     Obstacle(Vector2(6525 ,app.ground-190), 200,160, app.blockColor),
                     Obstacle(Vector2(6730,app.ground-90), 90,315, app.blockColor),
                     Obstacle(Vector2(7060,app.ground-180), 180,120, app.blockColor),
                     Obstacle(Vector2(7210,app.ground-280), 280,140, app.blockColor),
                     Obstacle(Vector2(7490 ,app.ground-190), 200,90, app.blockColor),
                     Obstacle(Vector2(7590,app.ground-95), 95,85, app.blockColor),
                     Obstacle(Vector2(7815, app.ground - 90),100, 85, app.blockColor),
                     Obstacle(Vector2(8005, app.ground - 190),50,190, app.blockColor),
                     Obstacle(Vector2(8535, app.ground - 90),100, 130, app.blockColor),
                     Obstacle(Vector2(8680, app.ground - 190),190, 130, app.blockColor),
                     Obstacle(Vector2(8845 , app.ground - 280),290, 110, app.blockColor),
                     Obstacle(Vector2(8975, app.ground - 380),390, 160, app.blockColor),
                     ]
    
    #Luckyblock position determined by hand, overlapping the hardCoded map.
    app.luckyBlock = Obstacle(Vector2(8332, 400),50, 50, app.blockColor)
    
    app.bowser = Enemy(Vector2(1110,220), 191,230,'black')
    app.bowserLife = 500
    
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
    app.player = Player(Vector2(app.playerX,app.playerY), 
                        app.playerHeight,app.playerWidth, app.playerColor)

def obstacle(app):
    app.blockWidth = 120
    app.blockHeight = 40
    app.blockX  = app.width
    app.blockY = app.ground - app.blockHeight
    app.blockRight = app.blockX + app.blockWidth
    app.blockBottom = app.blockY + app.blockHeight
    app.blockColor = None
    
    app.block = Obstacle(Vector2(app.blockX, app.blockY),
                         app.blockHeight, app.blockWidth, app.blockColor)
    
def rocket(app):
    app.rocketWidth = 95
    app.rocketHeight = 95
    app.rocketX = -app.rocketWidth
    app.rocketY = app.rocketHeight - app.rocketHeight
    
def redrawAll(app):

    if app.howToPlayScreen:
        drawImage('assets/SettingsPage.png',0,0) 
        
    elif app.gameWonScreen:
        drawImage('assets/GameWonScreen.png',0,0)
        drawLabel(f'{app.score}',app.width//2, 400, fill = 'white', size = 20)
    elif app.gameStartScreen:
        drawImage('assets/GameStartScreen.png',0,0)
        if app.hoverHowTo:
            drawImage('assets/rulesHover.png',480,400)
        else:
            drawImage('assets/Rules.png',480,400)
        if app.hoverStart:
            drawImage('assets/StartButtonHover.png',520,500)
        else:
            drawImage('assets/StartButton.png',520, 500)
        
    elif app.gameOver:
        drawImage('assets/GameOverScreen.png',0,0)
    elif app.pauseScreen:
        drawImage('assets/PausedScreen.png',0,0)
    
    
    else:
        drawBoard(app)
        drawPlayer(app)
        drawBullets(app)
        drawPlayer(app)
        drawEnemy(app)
        if app.bossBattle:
            drawPipe(app)
        
    
    debug(app)
    
#DEBUG MODE 
def debug(app):
    if app.debug:
        drawLine(0,app.floor,app.width,app.floor, fill = 'red')
        drawLine(0,app.ground,app.width,app.ground, fill = 'blue')
        drawLine(0, app.ceiling,app.width,app.ceiling,fill = 'yellow')
        drawLine(0,app.bulletFloor,app.width,app.bulletFloor, fill= 'green')
        for i in range(0, app.height,50):
            drawLine(0,i,app.width,i)
            drawLabel(f'{i}', 20, i+20)
        for i in range(0,app.width,50):
            drawLine(i,0,i,app.height)
            drawLabel(f'{i}', i +20, 20)
        drawLabel(f'x:{app.player.position.x}, y: {app.player.position.y}', app.centerPlayerX , app.centerPlayerY- 40, size = 12,fill = 'white')
        drawLabel(f'x:{app.scrollX}', app.centerPlayerX, app.centerPlayerY -100, size = 20,fill = 'black')
        for collider in ColliderObstacle.collidersObstacle:
            drawRect(collider.position.x, collider.position.y, collider.width, collider.height, fill = None, border = 'red')
        for collider in ColliderEnemy.collidersEnemy:
            drawRect(collider.position.x, collider.position.y, collider.width, collider.height, fill = None, border = 'red')
        drawRect(app.bowser.position.x,app.bowser.position.y,app.bowser.width,app.bowser.height,border = 'red')

def drawBoard(app):
    if app.bossBattle:
        drawBossBattle(app)
    else:
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
        drawImage('assets/luckyBlock.png', 8331 + app.scrollX,400)
        drawLabel(f'MARIO',200,40, size = 30 )
        drawLabel(f'Score:{app.score}',200,70, size = 30 )
        drawLabel(f'WORLD',app.width//2,40, size = 30 )
        drawLabel(f'1-1',app.width//2,70, size = 30 )
        drawLabel(f'TIME',1000, 40, size = 30 )
        drawLabel(f'{app.timeLeft}',1000,70, size = 30 )

#Positions with
def drawPipe(app):
    drawImage('assets/Pipe.png',-40,460)
    drawImage('assets/PipeVert.png', 200,-20)
    drawImage('assets/PipeVert.png', 500,-20)
    drawImage('assets/PipeVert.png', 800, -20)
    drawImage('assets/PipeLeft.png',1135,app.ground-150)
    drawImage(CMUImage(app.bottomImage),0,610)
    
def drawBossBattle(app):
    drawImage(CMUImage(app.marioBossMap),0,0)
    drawImage(CMUImage(app.bowserTitle),500,200)
    if app.bowserLife >= 20:
        drawRect(350,250,app.bowserLife,20,fill = 'red')
    drawRect(350,250,500,20, border = 'red',fill = None)
    
    
#------PLAYER CHARACTER--------
def drawPlayer(app):
    if not app.playerHide:
        if app.playerRunRight:
            sprite = app.sprites[app.spriteCounter]
            drawImage(sprite,app.player.position.x, app.player.position.y)
            if app.powerUp:
                drawImage('assets/Ak47.png',app.player.position.x+app.player.width-30,
                          app.player.position.y+(app.player.height)//2)
        elif app.playerRunLeft:
            spriteLeft = app.spritesLeft[app.spriteCounter]
            drawImage(spriteLeft,app.player.position.x, app.player.position.y)
        elif app.playerIdle:
            drawImage('assets/MarioIdle.png',app.player.position.x,app.player.position.y)
            if app.powerUp:
                drawImage('assets/Ak47.png',app.player.position.x+app.player.width-30, 
                          app.player.position.y+(app.player.height)//2)
        elif app.playerJumpRight:
            drawImage('assets/MarioJump.png',app.player.position.x, app.player.position.y)
            if app.powerUp:
                drawImage('assets/Ak47.png',app.player.position.x+app.player.width-30, 
                          app.player.position.y+(app.player.height)//2)
        elif app.playerJumpLeft:
            drawImage('assets/MarioJumpLeft.png',app.player.position.x,
                      app.player.position.y)

def drawEnemy(app):
    for enemy in app.enemies:
        if enemy.position.x < app.width + enemy.width:
            drawImage('assets/Koopa.png',enemy.position.x,enemy.position.y)
    if app.bossBattle:
        for rocket in app.rockets:
            drawImage(CMUImage(app.rocket),rocket.position.x,rocket.position.y)
        for shell in app.shells:
            drawImage(CMUImage(app.shell),shell.position.x, shell.position.y)
        drawImage(CMUImage(app.bowserImage), app.bowser.position.x, app.bowser.position.y)
        


def drawBullets(app):
    for bullet in Bullet.bullets:
       if app.powerUp:
            drawRect(bullet.position.x,bullet.position.y,
                     bullet.height,bullet.width, border = 'red')
       else:
            drawImage('assets/Fireball.png',bullet.position.x,bullet.position.y)
            
    for attack in app.bowserAttacks:
        drawRect(attack.position.x, attack.position.y, 
                 attack.height, attack.width, fill = 'red', border = 'red')

       
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
        app.pauseScreen = not app.pauseScreen
    if key == 'l':
        app.debug = not app.debug
    if key == 'w':
        if app.powerUp:
            slope = ((app.aimY - app.player.position.y)/ (app.aimX-app.player.position.x))
            Bullet(Vector2(app.player.position.x+ app.player.width, 
                           app.player.position.y + (app.player.height//2)),
                   20,10,slope,'player', 'red' )
        else:
            Bullet(Vector2(app.player.position.x+ app.player.width,
                           app.player.position.y + (app.player.height//2)),
                   43,42,0, 'player', 'red' )
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
        if app.bossBattle:
            if (('d' in app.keys and not app.stopMovementRight) and 
                (app.player.position.x + app.player.width< app.width)):
                app.player.moveRight()
                if 'space' not in app.keys:
                    app.playerRunRight = True
                    app.playerIdle = False
                    
        
                    
            
            elif (('a' in app.keys and app.player.position.x >0)
                  and not app.stopMovementLeft):
                    app.player.moveLeft()
                    if 'space' not in app.keys:
                        app.playerRunLeft = True
                        app.playerIdle = False
        else:
            if (('d' in app.keys and not app.stopMovementRight) and 
                (app.player.position.x + app.player.width< app.width)):
                if 'space' not in app.keys:
                    app.playerRunRight = True
                    app.playerIdle = False
                if (app.player.position.x < app.width//2 -100 or
                    (app.scrollX <= -8832)) :
                    app.player.moveRight()
                elif app.scrollX> -8832:
                    app.scrollX -= 9
                    
            
            elif (('a' in app.keys and app.player.position.x >0 )and 
                  not app.stopMovementLeft):
                if app.scrollX <= 0 and app.scrollX >= -8832:
                    app.player.moveLeft()
                    if 'space' not in app.keys:
                        app.playerRunLeft = True
                        app.playerIdle = False
                        
        if 'space' in app.keys and app.pressSpace: 
            app.player.jump(app)
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
    
    if app.paused: 
        if 520 <= mouseX  <= 758 and 520 <= mouseY<= 604:
            app.gameStartScreen = False
            app.paused = False
        if 480 <= mouseX <=790 and 400 <= mouseY<= 465:
            app.howToPlayScreen = True
        if 500 <= mouseY <= 575 and 175 <= mouseX <= 250:
            app.howToPlayScreen = False
    
        

def onMouseMove(app,mouseX,mouseY):
    app.aimX = mouseX
    app.aimY = mouseY
    if app.paused:
        if 520 <= mouseX  <= 758 and 520 <= mouseY<= 604:
            app.hoverStart = True
        elif 480 <= mouseX <=790 and 400 <= mouseY<= 465:
            app.hoverHowTo = True
        else:
            app.hoverHowTo = False
            app.hoverStart = False

def hitCeiling(app):
    if app.player.position.y < app.ceiling:
        app.falling = True
        app.player.position.y = app.ceiling
    
    elif app.falling:
        app.pressSpace = False
        app.player.isGrounded = False
        app.player.yVelocity += app.gravityInterval
            
def reloadEnemy(app):
    moveEnemy(app)
    for enemy in app.enemies: 
        enemy.position.x = enemy.startingX + app.scrollX
    if app.bowserLife <= 0:
        app.gameWon = True  
        app.gameWonScreen = True
        app.paused = True      
    Enemy.outOfBounds(app)
    
def reloadObstacle(app):
    for obstacle in app.obstacles: 
        obstacle.position.x = obstacle.startingX + app.scrollX
    app.luckyBlock.position.x = app.luckyBlock.startingX + app.scrollX

def reloadBullet(app):
    if app.bossBattle:
        for bullet in Bullet.bullets:
            if bullet.position.x > app.width:
                Bullet.bullets.remove(bullet)
        for attack in app.bowserAttacks:
            
            
            if 0>attack.position.x or 0>attack.position.y:
                app.bowserAttacks.remove(attack)
        
def moveEnemy(app):
    for enemy in app.enemies:
        for obstacle in ColliderObstacle.collidersObstacle:
            if ColliderEnemy.collidesRight(app,enemy,obstacle):
                    enemy.moveLeft = True
            if ColliderEnemy.collidesLeft(app,enemy,obstacle):
                    enemy.moveLeft = False
    for enemy in app.enemies:       
        if enemy.moveLeft:
            Enemy.moveLeft(enemy)
        else:
            Enemy.moveRight(enemy)
    if app.bossBattle:
        for rocket in app.rockets:
            Enemy.moveDown(rocket)
            if rocket.position.y > app.height:
                app.rockets.remove(rocket)
        for shell in app.shells:
            Enemy.slideLeft(shell)
            if shell.position.x < -app.shell.width:
                app.shells.remove(shell)

def bossBattle(app):
    if  app.bossBattleStart:
        
        app.ground = app.floor = 610
        if app.player.position.x >800:
            app.player.position.x = 0
        app.player.position.y = app.floor - app.player.height
        if app.player.position.x >=184:
            app.bossBattleStart = False
    if app.bossBattle:
        app.obstacles = [Obstacle(Vector2(0, app.ground - 140),150, 100, app.blockColor),
                         Obstacle(Vector2(1056, app.ground - 190),50, 250, app.blockColor),
                         Obstacle(Vector2(1140, app.ground - 140),150, 200, app.blockColor)]
        
def randomXvalue():
        location = random.randint(1,3)
        position =0
        if location == 1:
            position = 210
        elif location == 2:
            position= 510
        elif location == 3:
            position= 810
        
        return position
    
def bowserAttack(app):
    if app.ticks % 150 == 0 and app.bossBattle :
        app.bowserAttacks.append(Bullet(Vector2(1110, 220),
                                        20,20,0,'bowser', 'red' ))


def onStep(app):    
    
    if (not app.paused and not app.gameStartScreen and 
        not app.gameOver and not app.playerHide):
        app.ticks +=1
        if app.ticks % 400 == 0 and app.bossBattle:
            app.timerRocket += 50
            app.timerShell += 50
        if app.ticks % app.timerRocket == 0 and app.bossBattle:
            app.rockets.append(Enemy(Vector2(randomXvalue(), 
                                             app.rocketY), 95,95,'blue'))
            
            
        if app.ticks % app.timerShell == 0 and app.bossBattle:
            app.shells.append(Enemy(Vector2(app.width, app.ground - 85),
                                    75,75,'blue'))
        if app.ticks %5== 0 :
            app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
            
        if app.ticks %10 ==0 and not app.bossBattle and not app.paused:
             app.timeLeft -=1
        reloadEnemy(app)
        reloadObstacle(app)
        reloadBullet(app)
        playerIdle(app)
        
        bowserAttack(app)
        
        if ColliderBullet.isCollisionObstacle(app):
            Bullet.bullets.remove(app.bulletRemove)
            
        if ColliderEnemy.isCollision(app):
            Bullet.bullets.remove(app.bulletRemove)
            
        
    
        Enemy.load(app)
        app.player.applyGravity(app)
        bossBattle(app)
        Obstacle.obstacle(app)
        app.player.setYVelocity()
        app.player.playerDeath(app)
        app.player.playerWin(app)

        hitCeiling(app)
        
        if ColliderEnemy.collides(app.player,app.luckyBlock):
            app.powerUp = True
        Bullet.moveBullets(app)
        

runApp()