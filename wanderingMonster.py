import random
class WanderingMonster:
    # Defines random monster function
    def __init__(self, town_x, town_y):
        self.monster_x = 0
        self.monster_y = 0
        self.monster = self.new_random_monster()
        self.monster_color = self.monster['color']
        self.town_x = town_x
        self.town_y = town_y
        self.alive = True
    def __str__(self):
        return f'The Monster generated was {self.monster['name']} at position ({self.monster_x},{self.monster_y})'

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

        Example:
            >>>my_monster = WanderingMonster.new_random_monster(self)
            >>>print (my_monster['name'])
            A dragon
            >>>print (my_monster['description'])
            A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous
        """
        monster_number = random.randint(0, 5)  # collects random integer value
        # Following defines all monster possibilities
        monster_one = {
            'name': 'Dragon',
            'description':
                'A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous',
            'health': '300',
            'power': '450',
            'money': '125',
            'color': [153, 255, 255]}
        monster_two = {
            'name': 'Dragon',
            'description':
                "A deadly fire dragon. It's fire blasts bring death and destruction anywhere you go.",
            'health': '300',
            'power': '300',
            'money': '125',
            'color': [174, 75, 15]}
        monster_three = {
            'name': 'Elf',
            'description':
                'This Elf is from the long-beard woods and and has influence over nature.' 
                'It will entwine you with vines',
            'health': '100',
            'power': '80',
            'money': '70',
            'color': [180, 103, 77]}
        monster_four = {
            'name': 'Elf',
            'description':
                'This is a rock elf raised along stone river it'
                'commands the rocks and will use them against you if provoked',
            'health': '120',
            'power': '95',
            'money': '45',
            'color': [197, 197, 197]}
        monster_five = {
            'name': 'Ork',
            'description':
                'An ork is a creature little is understood about though '
                'their attacks are random they tend to prefer biting off their foes ankles',
            'health': '40',
            'power': '130',
            'money': '15',
            'color': [220, 220, 220]}
        monster_six = {
            'name': 'Piglin',
            'description':
                'Plated in gold Pigs are excellent swordsmen',
            'health': '175',
            'power': '200',
            'money': '250',
            'color': [255, 215, 0]}
        # combines all monster possibilities into one list
        monster_list = [monster_one, monster_two, monster_three, monster_four, monster_five, monster_six]
        # returns monster based on position in list and previously generate random integer
        return monster_list[monster_number]

    def move(self):
        if self.monster_x == 0 and self.monster_y == 288:
            self.monster_y -= 32
        elif self.monster_x == 0 and self.monster_y > 0:
            self.monster_y -= 32
        elif self.monster_x == 0 and self.monster_y == 0:
            self.monster_x += 32
        elif self.monster_x < 288 and self.monster_y < 288:
            self.monster_x += 32
        elif self.monster_x == 288 and self.monster_y < 288:
            self.monster_y += 32
        elif self.monster_x <= 288 and self.monster_y == 288:
            self.monster_x -= 32


        while self.monster_x == self.town_x and self.monster_y == self.town_y:
            if self.monster_x != 288 or self.monster_y != 288:
                if self.monster_x == self.town_x:
                    self.monster_x += 32
                elif self.monster_y == self.town_y:
                    self.monster_y += 32
    def death(self):
        self.alive = False
        self.monster_x = 500
        self.monster_y = 500

def monster_creation(town_x, town_y):
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