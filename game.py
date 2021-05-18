import random
import math
import time
from classes import Player, Creature


player_name = input('greetings prisoner. what should I call you?\n > ')
player = Player(player_name)

time.sleep(2.5)
print(f'hello, {player.name}...\n')

time.sleep(2.5)
print('you\'ve entered a dungeon from which there is no escape.\n')

time.sleep(2.5)
print(f'you have {player.attack} attack, {player.health} health, and {player.defense} defense.\n')

time.sleep(2.5)
print('you can wander through the dungeon, but you may encounter blood thirsty creatures\n')

time.sleep(3)
print('all you can do is battle them until you perish...\n')

time.sleep(4)
print('good luck...\n \n')

time.sleep(4)


kill_count = 0
innocent = 0
run_away = False
def morality_check(innocent, kill_count):
    if innocent == 0 and kill_count == 0:
        print('You didn\'t kill anything. did you not know how to play the game? how did you even get this score?')
    elif innocent == 0 and kill_count > 0:
        print('You didn\'t kill a single puppy or kitten. you are lawful good')
    elif kill_count > innocent:
        print('You killed more creatures than puppies and kittens. you were chaotic good')
    elif kill_count < innocent:
        print('You killed more puppies and kittens than anything. you were chaotic evil.')
    elif kill_count == innocent:
        print('You were meticulous and thoughtful in your killing... you are clearly evil in it\'s purest form')
    elif kill_count == 0 and innocent > 0:
        print('You ONLY killed puppies and kittens. You are a monster. You are pure evil. there is a spot reserved for you in the brand new tenth circle of hell.')
    pass

def fight(ent_a, ent_b):
    while ent_a.health > 0 and ent_b.health > 0: 
        damage = random.randint(1,6)
        time.sleep(1)
        command = input('press "a" to attack! "r to run away."\n > ')
        if command == 'a':
            if damage == 4 or damage == 2:
                time.sleep(1.5)
                print('YOU MISSED!')
                time.sleep(1)
                ent_a.health -= math.ceil(ent_b.attack / ent_a.defense)
                print(f'THE {ent_b.name} ATTACKED YOU FOR {ent_b.attack} DAMAGE!\n ')
                time.sleep(1.5)
                print(f'you have {player.health} health left...')
                continue
            if ent_a.health < 0:
                time.sleep(3)
                print(f'... welp. {ent_a.name}, you are super dead\n')
                break
            ent_b.health -= math.ceil(ent_a.attack / ent_b.defense)
            time.sleep(1)
            print(f'the {ent_b.name} has {ent_b.health} health left,\nand you have {ent_a.health} health left.\n ')
        else:
            time.sleep(1)
            print('fine. run away you wimp \n')
            run_away = True
            break

def game():

    acceptable_responses = ['fight', 'fight!', 'fuck it up', 'kill', 'kill it', 'attack', 'hit', 'stab', 'punch', 'kick', 'battle', 'kill it with fire', 'punch it in the face', 'smack', 'insult it\'s mom', 'thow tang at it']

    creature = Creature()
    global run_away
    global innocent
    global kill_count
    global game
        

    time.sleep(1)
    response = input(f'you\'ve encountered a {creature.name}!\nthe {creature.name} has {creature.attack} attack, {creature.health} health, and {creature.defense} defense,\nwhat will you do?\n > ')

    if response in acceptable_responses:
        fight(player, creature)
    else:
        run_away = True
        time.sleep(1)
        print('\nfine, wimp. next creature then...\n ')

    if run_away == False and player.health > 0: 
        if creature.name == 'PUPPY' or creature.name == 'KITTEN' and player.health > 0:
            innocent += 1
            time.sleep(2)
            print(f'congratulations. you killed the {creature.name}... you\'re aweful. You are a truely horrible person that deserves what fate has in store for you...\n ')
        else:   
            kill_count += 1
            time.sleep(2)
            print(f'congratulations. you killed the {creature.name}... it seems as if this is not the creature that will end you life...\n ')

    run_away = False

    if player.health <= 0:
        time.sleep(3)
        print(f'you had a good run, but your game is over....\n')
        time.sleep(3) 
        print(f'\nyou killed {kill_count} creatures, and {innocent} defenseless baby animals\n')
        game = False
        time.sleep(3)
        print('judgement...\n')
        time.sleep(3)
        morality_check(innocent, kill_count)     


while game:
    game()