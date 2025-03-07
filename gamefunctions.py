"""Contains operational functions for execution in an adventure game.

This module contains the functions: 
purchase_item(itemPrice, startingMoney, quantity)
new_random_monster()
print_welcome(name, width)
print_shop_menu(item1Name, item1Price, item2Name, item2Price)
these functions comprise what is required to create an adventure game.
"""
#gamefunctions.py
#Tucker Werhane
#March 7th, 2025
#This programs tests four functions, purchase_item, new_random_monster, print_welcome, and print_shop_menu.
#These functions can be called upon anywhere within the script to execute their predetrmined actions.

import random
# Defines purchase_item function
def purchase_item(itemPrice, startingMoney, quantity = 1):
    """
    Purchases a quantity of items at a specific price returning remaining balance.
    
    Parameters:
    itemPrice (float): The price of the item being purchased.
    startingMoney (float): The current money balance of the player.
    quantity (int): the number of items to purchase [Default value is 1]
    
    Returns:
    Quantity purchased (int): number of item purchased, if initial purchase quantity was too high 
    to be supported by starting balance then quantity is reduced.
    money_remain (float): money remaining after transaction.
    
    Example:
        >>>num_purchased, leftover_money = purchase_item(7.77, 300, 14)
        >>>print (num_purchased, 'items purchased.')
        14 items purchased.
        >>>print (leftover_money, 'money remaining.')
        191.22 money remaining.
        """
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
    """
    Generates Random monster along with it's stats.
        
    Parameters:
        None
        
    Returns:
        A monster with specified stats for:
            Name
            Description
            Health
            Power
            Money
    Example:
        >>>my_monster = new_random_monster()
        >>>print (my_monster['name'])
        A dragon
        >>>print (my_monster['description'])
        A powerful Ice dragon capable of much damage, but also much repair. Its Icy Breath is dangerous
    """
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
    """
    Creates a Welcome message.
        
    Parameters:
        name (str): A persons name.
        width (int): Width for the entire message [Default value is 20].
        
    Returns:
        None
        
    Prints:
        Welcome message
        
    Example:
        >>>print_welcome('Jeff')
            Hello, Jeff!    
        >>>print_welcome('Frank')
            Hello, Frank!    
    """
    welcome_string = 'Hello, ' + name + '!'
    print (f'{welcome_string :^{width}}')
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints a shop menu given two items and their prices.

    Parameters:
        item1Name (str): Name of first item to be presented in the shop.
        item1Price (float): Price of first item.
        item2Name (str): Name of second item presented in shop.
        item2Price (float): Price of second item.
    
    Returns:
        None
    
    Prints:
        Shop Menu: a table with two items and their prices.
    
    Examples:
        >>>print_shop_menu ("Sword", 57.72, "Heal Potion", 78)
        /----------------------\
        | Sword         $57.72 |
        | Heal Potion   $78.00 |
        \----------------------/
    """
    item1Price = (f'{float(item1Price):.2f}')
    item2Price = (f'{float(item2Price):.2f}')
    top_string = '/' + ('-' * 22) +'\\'
    bottom_string = '\\' + ('-' * 22) +'/'
    print (top_string)
    print(f'| {item1Name:<12}{('$' + item1Price):>8} |')
    print(f'| {item2Name:<12}{('$' + item2Price):>8} |')
    print (bottom_string)
#Function that tests all other functions in module
def test_functions():
    """Function runs tests on all other function in module"""
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
if __name__ == "__main__":
    test_functions()
