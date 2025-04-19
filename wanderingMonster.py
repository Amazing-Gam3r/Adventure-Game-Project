import random
class WanderingMonster:
    # Defines random monster function
    def __init__(self):
        self.monster_x = 0
        self.monster_y = 0
        self.monster = self.new_random_monster()
        self.monster_color = self.monster['color']

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
            'name': 'A Dragon',
            'description':
                'A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous',
            'health': '300',
            'power': '450',
            'money': '125',
            'color': [153, 255, 255]}
        monster_two = {
            'name': 'A Dragon',
            'description':
                "A deadly fire dragon. It's fire blasts bring death and destruction anywhere you go.",
            'health': '300',
            'power': '300',
            'money': '125',
            'color': [174, 75, 15]}
        monster_three = {
            'name': 'An Elf',
            'description':
                'This Elf is from the long-beard woods and and has influence over nature. It will entwine you with vines',
            'health': '100',
            'power': '80',
            'money': '70',
            'color': [180, 103, 77]}
        monster_four = {
            'name': 'An Elf',
            'description':
                'This is a rock elf raised along stone river it commands the rocks and will use them against you if provoked',
            'health': '120',
            'power': '95',
            'money': '45',
            'color': [197, 197, 197]}
        monster_five = {
            'name': 'A Ork',
            'description':
                'An ork is a creature little is understood about though '
                'their attacks are random they tend to prefer biting off their foes ankles',
            'health': '40',
            'power': '130',
            'money': '15',
            'color': [220, 220, 220]}
        monster_six = {
            'name': 'A Piglin',
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
        if self.monster_x <= 288:
            self.monster_x += 32
        elif self.monster_y <= 288:
            self.monster_y += 32
        elif self.monster_x == 0:
            self.monster_x -=32
        elif self.monster_y == 0:
            self.monster_y -= 32