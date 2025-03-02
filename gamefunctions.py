#gamefunctions.py
#Tucker Werhane
#Feburary 16th, 2025
#This programs tests two functions, purchase_item and new_random_monster.
#These functions can be called upon anywhere within the script to execute their predetrmined actions.


import random
# Defines purchase_item function
def purchase_item(itemPrice, startingMoney, quantity = 1):
    """Collects the price of an item current money balance and quanitity to be purchased 
    and outputs remaining balance after ensuring sufficent balance
    input: itemPrice, startingMoney, quantity
    Returns: tuple with quantity purchased, and money remaining"""
    purchase_yes = False
    while not purchase_yes: #loop allows program to deal with a item quantity request there is not funds for
        purchasing_price = itemPrice * quantity
        if purchasing_price > startingMoney:
            quantity = quantity - 1
        elif purchasing_price <= startingMoney:
            money_remain = startingMoney - purchasing_price
            purchase_yes = True
            money_remain = round(money_remain, 2)
            return quantity, money_remain
# Defines random mosnter function
def new_random_monster():
    """Using a preset list of amonsters and their attributes a random monster is slected and output
    no input"""
    monster_number = random.randint(0, 5) # collects random integer value
    #Following defines all monster possibilties
    monster_one = {
         'name': 'A Dragon', 
         'description': 
         'A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous', 
         'health': '300', 
         'power': '450', 
         'money': '125'}
    monster_two = {
         'name': 'A Dragon', 
         'description': 
         "A deadly fire dragon. It's fire blasts bring death and destruction anywhere you go.", 
         'health': '300', 
         'power': '300', 
         'money': '125'}
    monster_three = {
         'name': 'An Elf', 
         'description': 
         'This Elf is from the long-beard woods and and has influence over nature. It will entwine you with vines', 
         'health': '100', 
         'power': '80', 
         'money': '70'}
    monster_four = {
         'name': 'An Elf', 
         'description': 
         'This is a rock elf raised along stone river it commands the rocks and will use them aganist you if provoked', 
         'health': '120', 
         'power': '95', 
         'money': '45'}
    monster_five = {
         'name': 'A Ork', 
         'description': 
         'An ork is a creture little is understood about though ' 
         'their attacks are random they tend to prefer biting off their foes ankles', 
         'health': '40', 
         'power': '130', 
         'money': '15'}
    monster_six = {
         'name': 'A Piglin', 
         'description': 
         'Plated in gold Piglins are excellent swordsmen', 
         'health': '175', 
         'power': '200', 
         'money': '250'}
    # combines all monster possibilties into one list
    monster_list = [monster_one, monster_two, monster_three, monster_four, monster_five, monster_six]
    #returns monster based on postion in list and previously generate random integer
    return monster_list[monster_number]
def print_welcome(name, width = 20):
    """welcomes entered name into the game
    requires name input returns a printed welcome"""
    welcome_string = 'Hello, ' + name + '!'
    print (f'{welcome_string :^{width}}')
    
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Prints a menu with item names and their prices given two items and their prices
    requires item1Name, item1Price, item2Name, item2Price. Returns nothing"""
    item1Price = (f'{float(item1Price):.2f}')
    item2Price = (f'{float(item2Price):.2f}')
    top_string = '/' + ('-' * 22) +'\\'
    bottom_string = '\\' + ('-' * 22) +'/'
    print (top_string)
    print(f'| {item1Name:<12}{('$' + item1Price):>8} |')
    print(f'| {item2Name:<12}{('$' + item2Price):>8} |')
    print (bottom_string)
    
#Test conditions for purchase_item function
num_purchased, leftover_money = purchase_item(7.77, 300, 14)
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

num_purchased, leftover_money = purchase_item(56.93, 130, 4)
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

num_purchased, leftover_money = purchase_item(0.1, 20)
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

# test conditions for new_random_monster function
my_monster = new_random_monster()
print (my_monster['name'])
print (my_monster['description'])

my_monster = new_random_monster()
print (my_monster['name'])
print (my_monster['money'])

my_monster = new_random_monster()
print (my_monster['name'])
print (my_monster['health'])
print (my_monster['power'])

#Test conditions for print_welcome function using diffrent name lengths and differing field widths
print_welcome('Jeff')
print_welcome('Frank')
print_welcome('Carson')

#Test Conditions for print_shop_menu using varietys of items and prices
print_shop_menu ("Sword", 57.72, "Heal Potion", 78)
print_shop_menu ("Battle Axe", 178.525, "Cereal", 2.098766)
print_shop_menu ("Potatoes", 7, "Grapes", 14.98)
