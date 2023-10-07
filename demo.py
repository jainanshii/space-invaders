import pygame
import random
import math
x=pygame.init()

#creating window
window=pygame.display.set_mode((800,600))
pygame.display.set_caption("First game")

#game specific
background=pygame.image.load('backgground.jpg')

exit_game=False
exit_over=False
#player
iconplayer=pygame.image.load('space-invaders.png')
pX=370
pY=460
pX_change=0

#enemy
iconenemy=[]
eX=[]
eY=[]
eX_change=[]
ey_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
        iconenemy.append(pygame.image.load('enemy.png'))
        eX.append(random.randint(0,735))
        eY.append(random.randint(50,150))
        eX_change.append(0.3)
        ey_change.append(40)

#bullet
#ready:bullet is not seen on screen
#fire:bullet is fired
iconbullet=pygame.image.load('bullet.png')
bX=0
bY=480
bX_change=0
by_change=1
b_state="ready"


#score
score=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

game_font=pygame.font.Font('freesansbold.ttf',64)
#move
def player(x,y):
    window.blit(iconplayer,(x,y))
def enemy(x,y,i):
    window.blit(iconenemy[i],(x,y))
    #x+16 so that bullet is fired from center and y+!0 so that bullet is above the spaceship
def fire_bullet(x,y):
    global b_state
    b_state="fire"
    window.blit(iconbullet,(x+16,y+10))
def collision(x,y,bX,bY):
    distance=math.sqrt(math.pow(x-bX,2)+(math.pow(y-bY,2)))
    if distance<27:
        return True
    else:
        return False
def show_score(x,y):
    score_v=font.render("Score :"+str(score),True,(255,255,255))
    window.blit(score_v,(x,y))
def game_over_text():
    game_v=game_font.render("Game Over",True,(255,255,255))
    window.blit(game_v,(200,250))

#game loop
while not exit_game:
    window.fill((0,0,0,))
    window.blit(background,(0,0))
    player(pX,pY)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                pX_change=0.5
            if event.key==pygame.K_LEFT:
                pX_change=-0.5
            if event.key==pygame.K_SPACE:
               if b_state is"ready":
                    bX=pX
                    fire_bullet(bX,bY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pX_change=0
#to change player movement
    pX=pX+pX_change
    if pX<=0 :
        pX=0
    elif pX>=736:
        pX=736
    
    #enemy movement
    for i in range(num_of_enemies):
        #game over
        if eY[i]>440:
            for j in range(num_of_enemies):
                eY[j]=2000
            game_over_text()
            break
        eX[i]=eX[i]+eX_change[i]
        if eX[i]<=0 :
            eX_change[i]=0.3
            eY[i]+=ey_change[i]
        elif eX[i]>=736:
            eX_change[i]=-0.3
            eY[i]+=ey_change[i]
        
         #collision
        col=collision(eX[i],eY[i],bX,bY)
        if col:
            bY=480
            b_state="ready"
            score=score+1
            print(score)
            eX[i]=random.randint(0,735)
            eY[i]=random.randint(50,150)
        enemy(eX[i],eY[i],i)

    #bullet
    if bY<=0:
        bY=480
        b_state="ready"

    if b_state is "fire":
         fire_bullet(bX,bY)
         bY-=by_change

    #collision
    
    player(pX,pY)
    show_score(textX,textY)
    pygame.display.update()


pygame.quit()
quit()