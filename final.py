import pygame
import random
import time
import os

pygame.init()  # initialize the pygame
screen = pygame.display.set_mode((1500, 750))  # create screen (width,height)

running = True


class Player:                     #this is for easy access and shotening the code
    def __init__(
        self,
        name,
        x,
        y,
        position,
        img,
        color,
        ns=0,
        nc=0,
        np=0,
        jail=False,
        money=1500,
        properties_owned=[],
        truemoney=1500,
        total_pos=0,
    ):
        self.name = name
        self.x = x
        self.y = y
        self.position = position
        self.img = pygame.transform.scale(pygame.image.load(img), (32, 32))
        self.money = money
        self.properties_owned = properties_owned
        self.color = color
        self.np = np
        self.jail = jail
        self.truemoney = truemoney
        self.ns = ns
        self.nc = nc
        self.total_pos = total_pos


# boardposition:[positionx,positiony ]
positions = {
    0: [645, 650],
    1: [587, 650],
    2: [529, 650],
    3: [471, 650],
    4: [413, 650],
    5: [355, 650],
    6: [297, 650],
    7: [239, 650],
    8: [181, 650],
    9: [123, 650],
    10: [65, 650],
    11: [65, 592],
    12: [65, 534],
    13: [65, 476],
    14: [65, 418],
    15: [65, 360],
    16: [65, 302],
    17: [65, 244],
    18: [65, 186],
    19: [65, 128],
    20: [65, 70],
    21: [123, 70],
    22: [181, 70],
    23: [239, 70],
    24: [297, 70],
    25: [355, 70],
    26: [413, 70],
    27: [471, 70],
    28: [529, 70],
    29: [587, 70],
    30: [645, 70],
    31: [645, 128],
    32: [645, 186],
    33: [645, 244],
    34: [645, 302],
    35: [645, 360],
    36: [645, 418],
    37: [645, 476],
    38: [645, 534],
    39: [645, 592],
}
# assets and their values
assets = {
    1: ["old kent road.png", 60, 30, 33, 2, 4, 10, 30, 90, 160, 250, 50],
    3: ["whitechapel road.png", 60, 30, 33, 4, 8, 20, 60, 180, 320, 450, 50],
    6: ["the angel islington.png", 100, 50, 55, 6, 12, 30, 90, 270, 400, 550, 50],
    8: ["euston road.png", 100, 50, 55, 6, 12, 30, 90, 270, 400, 550, 50],
    9: ["pentonville road.png", 120, 60, 66, 8, 16, 40, 100, 300, 450, 600, 50],
    11: ["pall mall.png", 140, 70, 77, 10, 20, 50, 150, 450, 625, 750, 100],
    13: ["whitehall.png", 140, 70, 77, 10, 20, 50, 150, 450, 625, 750, 100],
    14: ["northumberland avenue.png", 160, 80, 88, 12, 24, 60, 180, 500, 700, 900, 100],
    16: ["bow street.png", 180, 90, 99, 14, 28, 70, 200, 550, 750, 950, 100],
    18: ["marlborough street.png", 180, 90, 99, 14, 28, 70, 200, 550, 750, 950, 100],
    19: ["vine street.png", 200, 100, 110, 16, 32, 80, 220, 600, 800, 1000, 100],
    21: ["the strand.png", 220, 110, 121, 18, 36, 90, 250, 700, 875, 1050, 150],
    23: ["fleet street.png", 220, 110, 121, 18, 36, 90, 250, 700, 875, 1050, 150],
    24: ["trafalgar square.png", 240, 120, 132, 20, 40, 100, 300, 750, 925, 1100, 150],
    26: ["leicester square.png", 260, 130, 143, 22, 44, 110, 330, 800, 975, 1150, 150],
    27: ["coventry street.png", 260, 130, 143, 22, 44, 110, 330, 800, 975, 1150, 150],
    29: ["piccadilly.png", 280, 140, 154, 24, 48, 120, 360, 850, 1025, 1200, 150],
    31: ["regent street.png", 300, 150, 165, 28, 52, 130, 390, 900, 1100, 1275, 200],
    32: ["oxford street.png", 300, 150, 165, 28, 52, 130, 390, 900, 1100, 1275, 200],
    34: ["bond street.png", 320, 160, 176, 28, 56, 150, 450, 1000, 1200, 1400, 200],
    37: ["park lane.png", 350, 175, 193, 35, 70, 175, 500, 1100, 1300, 1500, 200],
    39: ["mayfair.png", 400, 200, 220, 50, 100, 200, 600, 1400, 1700, 2000, 200],
}

railroads = {
    5: ["kingcross.png", 200, 100, 110, 25, 50, 100, 200],
    15: ["Marylebone.png", 200, 100, 110, 25, 50, 100, 200],
    25: ["Fenchurch.png", 200, 100, 110, 25, 50, 100, 200],
    35: ["Liverpool St..png", 200, 100, 110, 25, 50, 100, 200],
}

company = {12: ["electric company.png", 150, 75, 85], 28: ["water.png", 150, 75, 85]}

#rgb values of these colours[R,G,B]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [255, 0, 255]


def place_player(player):
    screen.blit(player.img, (player.x, player.y))


cas = [12, 28]
sas = [5, 15, 25, 35]

#assigning player their values
players = [
    Player(1, 645, 650, 0, "hat.png", red),
    Player(2, 675, 650, 0, "duck.png", blue),
    Player(3, 645, 680, 0, "ship.png", green),
    Player(4, 675, 680, 0, "dino.png", purple),
]

# game icon and title
pygame.display.set_caption("monopoly")
Icon = pygame.image.load("board-game.png")
pygame.display.set_icon(Icon)

# background
background = pygame.image.load("monopoly2.png")

font1 = pygame.font.SysFont("comicsans", 25)

#for printing a message.msg1 is text and j,k are x and y coordinates respectively colour 0,0,0 indicates black
def playermsg(msg1, j, k, color=[0, 0, 0]):
    msg = font1.render(msg1, True, (color))
    screen.blit(msg, (j, k))

#what happens after pressing y key on keyboard to buy something.it first subtracts cost (ignore turemoney)of the respective property then adds the property to the list of property owned by the player 
def ykey(player, assets):
    if player.position in assets:
        players[turn - 1].money -= assets[players[turn - 1].position][1]
        players[turn - 1].truemoney -= assets[players[turn - 1].position][2]
        props_owned = list(players[turn - 1].properties_owned)
        props_owned.append(players[turn - 1].position)
        players[turn - 1].properties_owned = props_owned

#this function checks if the property is already owned,if it isnt it blits a white screen containing the property image and texts
def buy_modal(player, assets):
    global players
    global np
    owned_by = None
    for p in players:
        for pos in p.properties_owned:
            if pos == player.position:
                owned_by = p  # player who owns the property

    if player.position in assets:
        if owned_by is None:
            pygame.draw.rect(screen, (255, 255, 255), (110, 110, 500, 500))
            screen.blit(
                pygame.transform.scale(
                    pygame.image.load(
                        "monopoly property/" + assets[player.position][0]
                    ),
                    (200, 312),
                ),
                (350, 250),
            )
            playermsg("Do you want to buy this property?", 200, 150)
            playermsg("Price: " + str(assets[player.position][1]), 200, 300)
            playermsg("Press Y to buy", 200, 400)
            playermsg("Press N to cancel", 200, 460)

#this function checks if the property is already owned,if it is then it subtracts the rent and blits a white screen displaying a text msg 
def rent_modal(player, assets, company, railroads, dice1, dice2):
    global players
    global np
    owned_by = None
    for p in players:
        for pos in p.properties_owned:
            if pos == player.position:
                owned_by = p  # player who owns the property

    if player.position in assets:
        if owned_by is not None:
            if owned_by.name == player.name:
                return
            pygame.draw.rect(screen, (255, 255, 255), (110, 110, 500, 500))
            playermsg(
                f"You paid {assets[player.position][4]} to player {owned_by.name}!",
                200,
                150,
            )
            if player.np == 0:  # np denotes if the player has paid rent once or not
                player.money -= assets[player.position][4]
                player.truemoney -= assets[player.position][4]
                for p in players:
                    if p.name == owned_by.name:
                        p.money += assets[player.position][4]
                        p.truemoney += assets[player.position][4]
                player.np = 1
    elif player.position in company:
        tdice = dice1 + dice2
        if owned_by is not None:
            if owned_by.name == player.name:
                return
            pygame.draw.rect(screen, (255, 255, 255), (110, 110, 500, 500))
            playermsg(
                f"You paid {4*tdice} to player {owned_by.name}!",
                200,
                150,
            )
            if player.np == 0:  # np denotes if the player has paid rent once or not
                if owned_by.nc == 1:
                    player.money -= 4 * tdice
                    player.truemoney -= 4 * tdice
                    for p in players:
                        if p.name == owned_by.name:
                            p.money += 4 * tdice
                            p.truemoney += 4 * tdice
                    player.np = 1
                if owned_by.nc == 2:
                    player.money -= 4 * tdice
                    player.truemoney -= 10 * tdice
                    for p in players:
                        if p.name == owned_by.name:
                            p.money += 10 * tdice
                            p.truemoney += 10 * tdice
                    player.np = 1
    elif player.position in railroads:
        if owned_by is not None:
            if owned_by.name == player.name:
                return
            pygame.draw.rect(screen, (255, 255, 255), (110, 110, 500, 500))
            playermsg(
                f"You paid {50*owned_by.ns} to player {owned_by.name}!",
                200,
                150,
            )
            if player.np == 0:  # np denotes if the player has paid rent once or not
                player.money -= 50 * owned_by.ns
                player.truemoney -= 50 * owned_by.ns
                for p in players:
                    if p.name == owned_by.name:
                        p.money += 50 * owned_by.ns
                        p.truemoney += 50 * owned_by.ns
                player.np = 1

#pick a number and load the  
def picknumber():
    dice1 = random.randint(1, 6)
    if dice1 == 1:
        dic1 = pygame.image.load("d1.png")
    elif dice1 == 2:
        dic1 = pygame.image.load("d2.png")
    elif dice1 == 3:
        dic1 = pygame.image.load("d3.png")
    elif dice1 == 4:
        dic1 = pygame.image.load("d4.png")
    elif dice1 == 5:
        dic1 = pygame.image.load("d5.png")
    elif dice1 == 6:
        dic1 = pygame.image.load("d6.png")
    return (dic1, dice1)# here only dice1 is enough it is a mistake(i m not changing it because the submitted code contains it)

#roll mechanism and placing the player 
def roll(player_idx, q, j, k):  # j=dice 1 xcoordinate q=dice2 xcor k=dice1and2 ycor
    dic1, dice1 = picknumber()
    dic2, dice2 = picknumber()
    td = dice1 + dice2
    screen.blit(dic1, (j, k))
    screen.blit(dic2, (q, k))
    for i in range(0, td):
        players[player_idx].position += 1
        players[player_idx].total_pos += 1
        if players[player_idx].position >= 40:
            players[player_idx].position = players[player_idx].position % 40
        players[player_idx].x = positions[players[player_idx].position][0]
        players[player_idx].y = positions[players[player_idx].position][1]
        place_player(players[player_idx])
        pygame.display.update()
        time.sleep(2)
    return dice1, dice2


#msg to print your turn
def yourTurnPrint(turn):
    msg2 = font1.render("Your turn", True, (255, 0, 0))
    screen.blit(msg2, (800, 150 * turn))

# turn will be 1 initially
turn = 1
#these are some variables
rolln = 0
q = 1
is_modal_open = False

while running:
    screen.fill((255, 255, 255))  # RGB (white)
    screen.blit(background, (0, 0))

    playermsg("Player 1", 1000, 150, players[0].color)
    playermsg("Player 2", 1000, 300, players[1].color)
    playermsg("Player 3", 1000, 450, players[2].color)
    playermsg("Player 4", 1000, 600, players[3].color)

    playermsg(str(players[0].money), 1000, 190)
    playermsg(str(players[1].money), 1000, 340)
    playermsg(str(players[2].money), 1000, 490)
    playermsg(str(players[3].money), 1000, 640)
    
    # playering
    for i, player in enumerate(players):
        screen.blit(players[i].img, (950, 150 * (i + 1)))

    yourTurnPrint(turn)
    if turn == 5:
        turn = 1
    
    if is_modal_open:
        buy_modal(players[turn - 1], assets)
        buy_modal(players[turn - 1], railroads)
        buy_modal(players[turn - 1], company)
        rent_modal(players[turn - 1], assets, railroads, company, dice1, dice2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# close button
            running = False
        if event.type == pygame.KEYDOWN: #if a key is pressed 
            if event.key == pygame.K_SPACE: #space key rolls the dice 
                rolln += 1
                if rolln > 1:
                    if dice1 == dice2:
                        q = 1
                    else:
                        q = 0
                if q == 1:
                    dice1, dice2 = roll(turn - 1, 1100, 1225, 150 * turn)
                    if dice1 != dice2:
                        q = 0
                    is_modal_open = True
                    players[turn - 1].np = 0
                    if players[turn - 1].position == 30:# jail 
                        players[turn - 1].position = 10
                        players[turn - 1].x = positions[players[turn - 1].position][0]
                        players[turn - 1].y = positions[players[turn - 1].position][1]
                        place_player(players[turn - 1])
                        pygame.display.update()
                        players[turn - 1].jail = True
                        players[turn - 1].money -= 50
                        time.sleep(0.2)
                    if (
                        players[turn - 1].position == 4
                        or players[turn - 1].position == 38
                    ):  # tax
                        players[turn - 1].money -= 200
                        players[turn - 1].truemoney -= 200
                    if players[turn - 1].position in [2, 17, 33]:#gifts
                        players[turn - 1].money += 50
                        players[turn - 1].truemoney += 50
                    if players[turn - 1].position in [7, 22, 36]:#tax
                        players[turn - 1].money -= 50
                        players[turn - 1].truemoney -= 50
                    # if players pass go then add 200 to their money
                    if players[turn - 1].total_pos >= 40:
                        players[turn - 1].money += 200
                        players[turn - 1].truemoney += 200
                        players[turn - 1].total_pos = players[turn - 1].total_pos % 40

            elif event.key == pygame.K_ESCAPE:#escape key changes the turn q ensures that one cannot roll twice
                if q != 1:
                    turn += 1
                    rolln = 0
                    q = 1
            elif event.key == pygame.K_y:
                if is_modal_open:
                    ykey(players[turn - 1], assets)
                    ykey(players[turn - 1], railroads)
                    ykey(players[turn - 1], company)
                    is_modal_open = False
                    if players[turn - 1].position in sas:
                        players[turn - 1].ns += 1
                    if players[turn - 1].position in cas:
                        players[turn - 1].nc += 1
            elif event.key == pygame.K_n:
                if is_modal_open:
                    is_modal_open = False
    
    for player in players:
        place_player(player)

    for player in players:
        for prop in player.properties_owned:
            x, y = positions[prop]
            if prop <= 10:
                pygame.draw.rect(screen, player.color, (x, y + 50, 15, 15))
            elif prop <= 20:
                pygame.draw.rect(screen, player.color, (x - 50, y, 15, 15))
            elif prop <= 30:
                pygame.draw.rect(screen, player.color, (x, y - 50, 15, 15))
            elif prop <= 40:
                pygame.draw.rect(screen, player.color, (x + 50, y, 15, 15))
    if player in players:
        if player.truemoney <= 0:
            playermsg(f"Player {player.name} is out of the game!", 200, 150)
            players.remove(player)
            turn -= 1
    pygame.display.update()
