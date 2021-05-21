import random

class Entity:

    def __init__(self):
        self.attack = random.randint(1,20)
        self.health = random.randint(1,20)
        self.defense = random.randint(2,8)


class Player(Entity):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        f'name: {self.name}, attack: {self.attack}, healh: {self.health}, defense: {self.defense}'


class Creature(Entity):

    def __init__(self):
        CREATURE_CAGE = ['BAT', 'CAT', 'RAT', 'SNAKE', 'TOAD', 'KITTEN', 'PUPPY']
        super().__init__()
        self.name = random.choice(CREATURE_CAGE)

    def __str__(self):
        return f'name: {self.name}, attack: {self.attack}, healh: {self.health}, defense: {self.defense}'

class Room:

    def __init__(self, name='. . ', north=None, south=None, east=None, west=None):
        self.inventory_of_room = dict()
        self.name = name
        self.north = None
        self.south = None
        self.east = None 
        self.west = None  

    def __str__(self):
        return f'{self.name}' 

class Dungeon:

    def __init__(self, rows, cols):
        self.layout = [[Room() for i in range(cols+1)] for j in range(rows+1)]

        def show_map(self):
            for row in self.layout:
                x = ""
                for col in row:
                    if 'player' in col.room:
                        col.name = '[O] '
                    if 'room' in col.room:
                        col.name = '[ ] '
                    if 'creature' in col.room:
                        col.name = '[+] '
                    x += col.name
                print(x)
    
    def place(self, key, value, row, col):
        '''
        a key is passed in along with the object/value in a given location
        '''
        location = self.layout[row][col]
        if key == 'p':
            location.room ['player'] = value
        if key == 'c':
            location.room['creature'] = value
            
def test():
    x = Dungeon(8,8)
    player = Player('seth')
    creature = Creature()
    x.place('p', player, 4, 4)
    x.place('c', creature, 4, 5)
    x.show_map()

    