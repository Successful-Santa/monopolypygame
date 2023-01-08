class Player:
    def __init__(self, name, x, y, position):
        self.name = name
        self.x = x
        self.y = y
        self.position = position

players = [
    Player(1, 645, 650, 0),
    Player(2, 675, 650 ,0),
    Player(3, 645, 680, 0),
    Player(4, 675, 680, 0),
]

def roll(player):
    player.position += 1

print(players[0].position)
print(players[1].position)
print("after roll")
roll(players[0])
roll(players[1])
print(players[0].position)
print(players[1].position)
