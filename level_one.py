from classes import Dungeon, Player, Creature

def north(level, x, y):
    north_room = level.layout[x+1][y]
    south_room = level.layout[x][y]
    north_room.south = True
    south_room.north = True

def south(level, x, y):
    north_room = level.layout[x][y]
    south_room = level.layout[x-1][y]
    north_room.south = True
    south_room.north = True

def east(level, x, y):
    east_room = level.layout[x][y+1]
    west_room = level.layout[x][y]
    east_room.west = True
    west_room.east = True

def west(level, x, y):
    east_room = level.layout[x][y]
    west_room = level.layout[x][y-1]
    east_room.west = True
    west_room.east = True


def level_one():
    level = Dungeon(8,8)
    east(level,0,0)
    east(level,0,1)
    east(level,0,2)
    east(level,0,3)
    east(level,0,4)
    level.layout[0][5].west = False

    level.layout[0][4].north = False
    south(level,0,4)
    south(level,1,4)
    south(level,2,4)
    south(level,3,4)
    south(level,4,4)
    
    return level

def test():
    x = level_one()
    player = Player('seth')
    creature = Creature()
    x.place('p', player, 4, 4)
    x.place('c', creature, 4, 5)
    x.show_map()