from classes import Dungeon, Player, Creature

def auto_map(level, key, w, h):
    x = 0
    y = 0
    for row in key:

        for col in row:

            if x + 1 < w:
                if key[x][y] == 1:
                    if key[x+1][y] == 1:
                        level.layout[x][y].north = True

            if x- 1 > 0:
                if key[x][y] == 1:
                    if key[x-1][y] == 1:
                        level.layout[x][y].south = True

            if y + 1 < h:
                if key[x][y] == 1:
                    if key[x][y+1] == 1:
                        level.layout[x][y].east = True

            if y - 1 > 0:
                if key[x][y] == 1:
                    if key[x][y-1] == 1:
                        level.layout[x][y].west == True

            y += 1                                             
        y = 0
        x += 1

    return level


def test():
    first_map = [
    [0,1,0,1,1,1,1,0,1],
    [0,1,0,0,0,0,1,1,1],
    [0,1,1,1,1,1,1,1,1],
    [0,1,0,0,0,0,1,0,1],
    [0,0,1,1,1,1,1,0,1],
    [0,1,1,0,0,0,1,0,1],
    [1,1,0,1,1,1,0,0,1],
    [0,1,0,1,0,1,0,0,1],
    [0,1,1,1,0,1,1,1,1],
    ]

    x = Dungeon(8,8)
    y = auto_map(x,first_map,8,8)
    player = Player('seth')
    creature = Creature()
    y.place('p', player, 4, 4)
    y.place('c', creature, 4, 5)
    y.show_map()