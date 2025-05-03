"""Contains the componets required to create, generate, move, and regenerate fightable monsters for an adventure game.

This module contains the function:
    monster_creation(town_x, town_y):

This module also contains the classes:
    WanderingMonster(town_x, town_y): used to generate and move fightable monsters.

Combined these functions and classes produce fightable monsters.
"""

#wanderingMonster.py
#Tucker Werhane
#May 4th, 2025
#This module generates fightable monsters.

import random #used for genertaing random positions on a map

class WanderingMonster:
    """WanderingMonster class to generate and move fightable monsters.

    Instance Objects:
        monster_x (int): x coordinate of the monster in the class instance.
        monster_y (int): y coordinate of the monster in the class instance.
        monster (dict): stats of monster generated for class instance.
        monster_color (color): the color of the monster in the class instance.
        moncter_image (str): the path to the image of the monster.
        town_x (int): x coordinate of the town in the class instance.
        town_y (int): y coordinate of the town in the class instance.
        alive (bool): if the monster is alive or not.
        player_moves (int): the number of moves the player has made on the map.

    Methods:
        new_random_monster(): generates a new monster.
        move(): moves the monster around the map.
        death(): used to move monster off map after the monster is killed.
        """

    # Defines random monster function
    def __init__(self, town_x, town_y):
        """Intializes WanderingMonster class.

        Parameters:
            town_x (int): x coordinate of the town in the class instance.
            town_y (int): y coordinate of the town in the class instance.

        Example:
            >>my_monster = WanderingMonster(64, 128)
            >>print(my_monster.monster["name"]
            Dragon
            """
        self.monster_x = 0
        self.monster_y = 0
        self.monster = self.new_random_monster()
        self.monster_color = self.monster['color']
        self.monster_image = self.monster['image'] #image for monster
        self.town_x = town_x
        self.town_y = town_y
        self.alive = True
        self.player_moves = 0

    def __str__(self):
        """Formats string output when instnace is printed.

        Example:
            >>monster_test = WanderingMonster(64, 128)
            >>print(monster_test)
            Piglin at Color: [255, 215, 0] at location: (64, 128)"""

        return f'{self.monster['name']} at Color: {self.monster_color} at location: ({self.town_x}, {self.town_y})'

    def new_random_monster(self):
        """
        Generates Random monster along with its stats.

        Returns:
            A monster with specified stats for:
                Name
                Description
                Health
                Power
                Money
                Color

        Example:
            >>my_monster = WanderingMonster.new_random_monster()
            >>print (my_monster['name'])
            A dragon
            >>print (my_monster['description'])
            A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous
        """
        monster_number = random.randint(0, 5)  # collects random integer value
        # Following defines all monster possibilities
        monster_one = {
            'name': 'Ice Dragon',
            'description':
                'A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous',
            'health': '300',
            'power': '450',
            'money': '125',
            'color': [153, 255, 255],
            'image': 'ice_dragon'}
        monster_two = {
            'name': 'Fire Dragon',
            'description':
                "A deadly fire dragon. It's fire blasts bring death and destruction anywhere you go.",
            'health': '300',
            'power': '300',
            'money': '125',
            'color': [174, 75, 15],
            'image': 'fire_dragon'}
        monster_three = {
            'name': 'Vine Elf',
            'description':
                'This Elf is from the long-beard woods and and has influence over nature.' 
                'It will entwine you with vines',
            'health': '100',
            'power': '80',
            'money': '70',
            'color': [180, 103, 77],
            'image': 'vine_elf'}
        monster_four = {
            'name': 'Rock Elf',
            'description':
                'This is a rock elf raised along stone river it'
                'commands the rocks and will use them against you if provoked',
            'health': '120',
            'power': '95',
            'money': '45',
            'color': [197, 197, 197],
            'image': 'rock_elf'}
        monster_five = {
            'name': 'Orc',
            'description':
                'An orc is a creature little is understood about though '
                'their attacks are random they tend to prefer biting off their foes ankles',
            'health': '40',
            'power': '130',
            'money': '15',
            'color': [220, 220, 220],
            'image': 'orc'}
        monster_six = {
            'name': 'Piglin',
            'description':
                'Plated in gold Pigs are excellent swordsmen',
            'health': '175',
            'power': '200',
            'money': '250',
            'color': [255, 215, 0],
            'image': 'piglin'}
        # combines all monster possibilities into one list
        monster_list = [monster_one, monster_two, monster_three, monster_four, monster_five, monster_six]
        # returns monster based on position in list and previously generate random integer
        return monster_list[monster_number]

    def move(self):
        """Moves monster around the map every other time the player moves.

        Follows pattern that eventually ends with monsters circling map border

        Example:
            >>my_monster = WanderingMonster(256, 256)
            print(my_monster.monster_x, my_monster.monster_y)
            0 0
            >>my_monster.move()
            print(my_monster.monster_x, my_monster.monster_y)
            32 0
        """
        #increments player moves and moves monsters every other player move
        self.player_moves += 1
        if self.player_moves % 2 == 0:
            if self.monster_x == 0 and self.monster_y == 288: #starts to move monsters up left border of map
                 self.monster_y -= 32
            elif self.monster_x == 0 and self.monster_y > 0: #moves monsters up left border of map
                self.monster_y -= 32
            elif self.monster_x == 0 and self.monster_y == 0: #Starts moving monster right along top border
                self.monster_x += 32
            elif self.monster_x < 288 and self.monster_y < 288: #moves player to right border
                self.monster_x += 32
            elif self.monster_x == 288 and self.monster_y < 288: #moves player down along right border
                self.monster_y += 32
            elif self.monster_x <= 288 and self.monster_y == 288: #moves player left along bottom border
                self.monster_x -= 32

            while self.monster_x == self.town_x and self.monster_y == self.town_y: #skips monster over town if needed
                if self.monster_x != 288 or self.monster_y != 288:
                    if self.monster_x == self.town_x:
                        self.monster_x += 32
                    elif self.monster_y == self.town_y:
                        self.monster_y += 32

    def death(self):
        """Updates monsters alive status to dead and move monster off map.

        Example:
            >>my_monster = WanderingMonster(128, 256)
            >>print(my_monster.alive)
            True
            >>my_monster.death()
            >>print(my_monster.alive)
            False
            """
        self.alive = False #monster is dead
        #moves dead monster outside playable border so no fight can be triggered
        self.monster_x = 500
        self.monster_y = 500

def monster_creation(town_x, town_y):
    """ creates monsters using wanderingMonster class.

    Parameters:
        town_x (int): x coordinate of town.
        town_y (int): y coordinate of town.

    Returns:
        monster1 (class instance): a monster the player can fight
        monster2 (class instance): a second monster the player can fight

    Example:
        >>monster1, monster2 = monster_creation(128, 128)
        >>print(monster1)
        Piglin at Color: [255, 215, 0] at location: (128, 128)
        >>print(monster2)
        Dragon at Color: [153, 255, 255] at location: (128, 128)
        """
    monster1 = WanderingMonster(town_x, town_y)
    # Randomly creates coordinate for monster1 circle
    monster1.monster_x = random.randint(0, 9) * 32
    monster1.monster_y = random.randint(0, 9) * 32

    # Ensures monster1 location is not the same as the town location
    while (monster1.monster_x == town_x) and (monster1.monster_y == town_y):
        monster1.monster_x = random.randint(0, 9) * 32
        monster1.monster_y = random.randint(0, 9) * 32

    monster2 = WanderingMonster(town_x, town_y)
    # Randomly creates coordinate for monster1 circle
    monster2.monster_x = random.randint(0, 9) * 32
    monster2.monster_y = random.randint(0, 9) * 32

    # Ensures monster2 location is not the same as the town or monster1 location
    while (((monster2.monster_x == town_x) and (monster2.monster_y == town_y)) or
           ((monster2.monster_x == monster1.monster_x) and (monster2.monster_y == monster1.monster_y))):
        monster2.monster_x = random.randint(0, 9) * 32
        monster2.monster_y = random.randint(0, 9) * 32
    return monster1, monster2

if __name__ == '__main__':
    #WanderingMonster Class Initilization test
    my_monster = WanderingMonster(64, 128)
    print(my_monster.monster["name"])

    #WanderingMonster Class string format test:
    monster_test = WanderingMonster(64, 128)
    print(monster_test)

    #move function test:
    my_monster = WanderingMonster(256, 256)
    print(my_monster.monster_x, my_monster.monster_y)
    my_monster.move()
    print(my_monster.monster_x, my_monster.monster_y)

    #death function test:
    my_monster = WanderingMonster(128, 256)
    print(my_monster.alive)
    my_monster.death()
    print(my_monster.alive)

    #monster creation test:
    monster1, monster2 = monster_creation(128, 128)
    print(monster1)
    print(monster2)