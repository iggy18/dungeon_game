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
     self.layout = [[Room() for i in range(cols)] for j in range(rows)]

    def show_map(self):
        for row in self.layout:
            x = ""
            for col in row:
                x += col.name
            print(x)

    def add_room(self, row, col, name):
        location = self.layout[row][col]
        location.name = name

    def connect_rooms(self, row, col, n=None, s=None, e=None, w=None):
        location = self.layout[row][col]
        if location.north is not None:
            location.north = location

    