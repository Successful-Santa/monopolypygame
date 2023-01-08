import pygame
import random
import time


pygame.init()# initialize the pygame
screen=pygame.display.set_mode((1500,750))#create screen (width,height)

running=True

#players
playerimg1=pygame.image.load("hat.png")
playerimg1=pygame.transform.scale(playerimg1,(32, 32))
playerx1=645
playery1=650
playerimg2=pygame.image.load("duck.png")
playerimg2=pygame.transform.scale(playerimg2,(32, 32))
playerx2=675
playery2=650
playerimg3=pygame.image.load("dino.png")
playerimg3=pygame.transform.scale(playerimg3,(32, 32))
playerx3=645
playery3=680
playerimg4=pygame.image.load("ship.png")
playerimg4=pygame.transform.scale(playerimg4,(32, 32))
playerx4=675
playery4=680

def player(t,x,y):
    screen.blit(t,(x,y))

#game icon and title
pygame.display.set_caption("monopoly")
Icon=pygame.image.load("board-game.png")
pygame.display.set_icon(Icon)

# #button
# buybuttonimg=pygame.image.load("buybutton.png")
# buybuttonimg=pygame.transform.scale(buybuttonimg,(40,40))
# button=pygame.rect(100,100,30,30) #positionx,y and size l,b

#background
background = pygame.image.load("monopoly2.png")

font1= pygame.font.SysFont("comicsans",25)

def roll(playerimg,playerx,playery,playerposition,q,j,k):#j=dice 1 xcoordinate q=dice2 xcor k=dice1and2 ycor 
    dic1, dice1 = picknumber()
    dic2, dice2 = picknumber()
    td = dice1 + dice2
    screen.blit(dic1, (j,k))
    screen.blit(dic2, (q,k))
    for i in range(0, td):
        playerposition += 1
        if playerposition >= 40:
            playerposition = playerposition % 40

        playerx = d[playerposition][0]
        playery = d[playerposition][1]
        player(playerimg, playerx, playery)
        pygame.display.update()
        time.sleep(0.5)
    return playerx,playery,playerposition,dice1,dice2

def playermsg(msg1,j,k):
    msg=font1.render(msg1,True,(0,0,0))
    screen.blit(msg,(j,k))
def turns():
    msg2=font1.render("Your turn",True,(255,0,0))
    if turn== 1:
        screen.blit(msg2,(800,150))
    if turn == 2:
        screen.blit(msg2,(800,300))
    if turn == 3:
        screen.blit(msg2,(800,450))
    if turn == 4 :
        screen.blit(msg2,(800,600))
msgp1="player 1"
msgp2="player 2"
msgp3="player 3"
msgp4="player 4"
#position
d={0: [645, 650], 1: [587, 650], 2: [529, 650], 3: [471, 650], 4: [413, 650], 5: [355, 650], 6: [297, 650], 7: [239, 650], 8: [181, 650], 9: [123, 650], 10: [65, 650],
    11: [65, 592], 12: [65, 534], 13: [65, 476], 14: [65, 418], 15: [65, 360], 16: [65, 302], 17: [65, 244], 18: [65, 186], 19: [65, 128], 20: [65, 70],
    21: [123, 70], 22: [181, 70], 23: [239, 70], 24: [297, 70], 25: [355, 70], 26: [413, 70], 27: [471, 70], 28: [529, 70], 29: [587, 70], 30: [645, 70],
    31: [645, 128], 32: [645, 186], 33: [645, 244], 34: [645, 302], 35: [645, 360], 36: [645, 418], 37: [645, 476], 38: [645, 534], 39: [645, 592]}
#assets
d1={1:"old kent road.png",3:"whitechapel road.png",6:"the angel islington.png",8:"euston road.png",9:"pentonville road.png",11:"pall mall.png",
    13:"whitehall.png",14:"northumberland avenue.png",16:"bow street.png",18:"marlborough street.png",19:"vine street.png",21:"strand.png",
    23:"fleet street.png",24:"trafalgar square.png",26:"leicester.png",27:"coventry street.png",29:"piccadilly.png",31:"regent street.png",
    32:"oxford street.png",34:"bond street.png",37:"park lane.png",39:"mayfair.png"}
def assets(playerposition):
    if playerposition in d1:
        lkj=pygame.image.load('monopoly property/'+d1[playerposition])
        lkj=pygame.transform.scale(lkj, (150, 300))
        screen.blit(lkj,(300,300))




#dice
def picknumber():
    dice1=random.randint(1,6)
    if dice1== 1 :
        dic1=pygame.image.load("d1.png")
    elif dice1== 2 :
        dic1=pygame.image.load("d2.png")
    elif dice1== 3 :
        dic1=pygame.image.load("d3.png")
    elif dice1== 4 :
        dic1=pygame.image.load("d4.png")
    elif dice1== 5 :
        dic1=pygame.image.load("d5.png")
    elif dice1== 6 :
        dic1=pygame.image.load("d6.png")
    return(dic1,dice1)                             



turn=1
rolln=0
q=1
playerposition1=0
playerposition2=0
playerposition3=0
playerposition4=0
playermoney1=1500
playermoney2=1500
playermoney3=1500
playermoney4=1500
# game loop
while running:
    screen.fill((255, 255, 255))  # RGB
    screen.blit(background,(0,0))
    playermsg(msgp1,1000,150)
    playermsg(msgp2,1000,300)
    playermsg(msgp3,1000,450)
    playermsg(msgp4,1000,600)

    turns()
    if turn==5:
        turn=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if a keystroke is pressed check whether its space
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                rolln+=1
                if turn==1:
                    if rolln>1:
                        if dice11==dice21:
                            q=1
                        else:
                            q=0
                    if q == 1:
                        playerx1,playery1,playerposition1,dice11,dice21 = roll(playerimg1,playerx1,playery1,playerposition1,1100,1225,150)
                        if dice11!=dice21:
                            q=0



                if turn==2:
                    if rolln>1:
                        if dice12==dice22:
                            q=1
                        else:
                            q=0
                    if q == 1:
                        playerx2,playery2,playerposition2,dice12,dice22= roll(playerimg2, playerx2, playery2, playerposition2,1100,1225, 300)
                        if dice12!=dice22:
                            q=0
                if turn==3:
                    if rolln>1:
                        if dice13==dice23:
                            q=1
                        else:
                            q=0
                    if q == 1:
                        playerx3,playery3,playerposition3,dice13,dice23=roll(playerimg3, playerx3, playery3, playerposition3, 1100,1225, 450)
                        if dice13!=dice23:
                            q=0
                if turn==4:
                    if rolln>1:
                        if dice14==dice24:
                            q=1
                        else:
                            q=0
                    if q==1:
                        playerx4,playery4,playerposition4,dice14,dice24 =roll(playerimg4, playerx4, playery4, playerposition4, 1100,1225, 600)
                        if dice14!=dice24:
                            q=0

            if event.key == pygame.K_ESCAPE:
                if q!=1:
                    turn+=1
                    rolln=0
                    q=1
        # elif event.type==pygame.MOUSEBUTTONDOWN:
        #     mouse_pos=pygame.mouse.get_pos()
        #     if button.collidepoint(mouse_pos):
        #         pass
                


    if turn==1:
        assets(playerposition1)
    if turn==2:
        assets(playerposition2)
    if turn==3:
        assets(playerposition3)
    if turn==4:
        assets(playerposition4)




    if playerx1 <= 65:
        playerx1=65
    elif playerx1>645:
        playerx1=645
    if playery1<=70:
        playery1=70
    elif playery1>650:
        playery1=650
    playermsg(str(playermoney1), 1000, 190)
    playermsg(str(playermoney2), 1000, 340)
    playermsg(str(playermoney3), 1000, 490)
    playermsg(str(playermoney4), 1000, 640)
    player(playerimg1,playerx1, playery1)
    player(playerimg2, playerx2, playery2)
    player(playerimg3, playerx3, playery3)
    player(playerimg4, playerx4, playery4)
    player(playerimg1, 950, 150)
    player(playerimg2, 950, 300)
    player(playerimg3, 950, 450)
    player(playerimg4,950,600)
    pygame.display.update()

