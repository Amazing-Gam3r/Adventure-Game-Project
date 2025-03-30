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
#March 8th, 2025
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
#a function that a Prints welcome sign 
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
    #Combines name with welcome string
    welcome_string = 'Hello, ' + name + '!'
    print (f'{welcome_string :^{width}}')
#a function that prints a shop menu
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
    #formats item lisitngs
    item1Price = (f'{float(item1Price):.2f}')
    item2Price = (f'{float(item2Price):.2f}')
    #formats maneu design
    top_string = '/' + ('-' * 22) +'\\'
    bottom_string = '\\' + ('-' * 22) +'/'
    #prints menu
    print (top_string)
    print(f'| {item1Name:<12}{('$' + item1Price):>8} |')
    print(f'| {item2Name:<12}{('$' + item2Price):>8} |')
    print (bottom_string)
#main game menu
def town_menu(hp, gold):
    """
    Prints a initial menu for actions to be taken within the game.
    
    Parameters:
        hp (int): The amount of health the player currently has.
        gold (float): The current amount of gold the player has.
    Returns:
        user_choice: A value of 1, 2, or 3 that corresponds to a specific action set.
    
    Prints:
        Town menu: prints a list of possible actions taken
    
    Examples:
        >>>print(town_menu(45, 62))
        You are in town.
        Current HP: 45, Current Gold: 62
        What would you like to do?
        1) Leave town (Fight Monster)
        2) Sleep (Restore HP for 15 Gold)
        3) Quit
    """
    #Prints options and welcome
    print ('You are in town.')
    print (f'Current HP: {hp}, Current Gold: {gold}')
    user_choice = input('What would you like to do?\n\n'
                        '1) Leave town (Fight Monster)\n'
                        '2) Sleep (Restore HP for 10 Gold)\n'
                        '3) Quit\n')
    #validates users choice
    user_choice = validate_answer3(user_choice)
    return user_choice
# Displays current fight statistics    
def displayFightStatistics(user_hp, monster_hp, monster_name = 'Monster'):
    """
    Displays current health of player and monster being fought.
    
    Parameters:
        user_hp (int): Current health level of player.
        monster_hp (int): Current health of monster.
        monster_name (str): Name of monster being fought. [Defaults to Monster]
    Returns:
        None
    Prints:
        Fight_statistics: Displays current health of player and monster.
    Examples:
        >>>displayFightStatistics(48, 153, Dragon)
        Your health is currently 48 HP.
        The Dragon is at 153 HP.  
    """
    #prints statistics
    print(f'Your health is currently {user_hp} HP.\nThe {monster_name} is at {monster_hp} HP.')
#Function that prints menu of fight options
def getUserFightOptions(user_hp, gold, monster_hp, monster_name):
    """
    Menu and selection for options in a fight.
    
    Parameters:
        user_hp (int): Current health of the user.
        gold (float): Current gold balance of the player.
        monster_hp (int): The health of the monster.
        monster_name (str): The monsters name.
    Returns:
        user_choice: a value of 1, 2, or 3 pertaining to the users chocie in the menu.
    Examples:
        >>>print(getUserFightOptions(50, 17, 42, 'Goblin'))
        Your health is currently 50 HP.
        The Goblin is at 42 HP.
        (Current Gold: 17) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 1 Gold)
        >>>1
        1
    """
    displayFightStatistics(user_hp, monster_hp, monster_name)
    print (f'(Current Gold: {gold}) \nHow would you like to continue?')
    #Determines players move choice for the fight
    user_choice = input('1) Primary Attack (5-37 damage)\n'
                        '2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)\n'
                        '3) Leave fight (Lose 10 Gold)\n')
    sufficency = False
    while sufficency == False:
        user_choice = validate_answer3(user_choice)
        if user_choice == 2:
            sufficency = gold_check(gold, 5)
            user_choice = input()
        else:
            sufficency = True
    return user_choice
#Fight Sequence Function
def monster_fight(hp, gold):
    """
    Conducts a fight sequence against a monster.
    
    Parameters:
        hp (int): Current health of player.
        gold (float): Current money held by the player
    Returns: hp, gold
        hp (int): remaining player health after battle.
        gold (float) remaing gold held by player after battle.
    Examples:
        >>>print (monster_fight(400, 17))
        You are fighting An Elf.
        This monster has 120 HP and 95 power.

        Your health is currently 400 HP.
        The An Elf is at 120 HP.
        (Current Gold: 17) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>2
        5 Gold spent on Shield Potion
        The monster did 10 damage, your shield repeled the damage,as a result the monster lost 5.0 HP leaving it at 115.0 HP

        Your health is currently 400 HP.
        The An Elf is at 115.0 HP.
        (Current Gold: 12) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>1
        Your attack yields 25 damage
        The monster has 90.0 HP remaining
        The monster did 91 damage, leaving you with 309 HP

        Your health is currently 309 HP.
        The An Elf is at 90.0 HP.
        (Current Gold: 12) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>1
        Your attack yields 19 damage
        The monster has 71.0 HP remaining
        The monster did 40 damage, leaving you with 269 HP

        Your health is currently 269 HP.
        The An Elf is at 71.0 HP.
        (Current Gold: 12) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>1
        Your attack yields 6 damage
        The monster has 65.0 HP remaining
        The monster did 26 damage, leaving you with 243 HP

        Your health is currently 243 HP.
        The An Elf is at 65.0 HP.
        (Current Gold: 12) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>1
        Your attack yields 9 damage
        The monster has 56.0 HP remaining
        The monster did 83 damage, leaving you with 160 HP

        Your health is currently 160 HP.
        The An Elf is at 56.0 HP.
        (Current Gold: 12) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>2
        5 Gold spent on Shield Potion
        The monster did 27 damage, your shield repeled the damage,as a result the monster lost 13.5 HP leaving it at 42.5 HP

        Your health is currently 160 HP.
        The An Elf is at 42.5 HP.
        (Current Gold: 7) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>2
        5 Gold spent on Shield Potion
        The monster did 69 damage, your shield repeled the damage,as a result the monster lost 34.5 HP leaving it at 8.0 HP

        Your health is currently 160 HP.
        The An Elf is at 8.0 HP.
        (Current Gold: 2) 
        How would you like to continue?
        1) Primary Attack (5-37 damage)
        2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)
        3) Leave fight (Lose 10 Gold)
        >>>1
        Your attack yields 10 damage
        The monster has -2.0 HP remaining
        The monster did 10 damage, leaving you with 150 HP

        Fight over
        You killed the monster.
        You won 1 Gold from the battle.
        You have gained 25 health from winning
        (175, 3)
    """
    #Selects random monster
    monster=new_random_monster()
    name = monster['name']
    print(f'You are fighting {name}.')
    monster_health = int(monster['health'])
    monster_power = int(monster['power'])
    print(f'This monster has {monster_health} HP and {monster_power} power.\n')
    fight = True
    #fight sequence loop
    while fight == True:
        #Death of monster or player
        if hp <= 0 or monster_health <= 0:
            hp, gold = fight_death(hp, gold, monster_health, monster['money'])
        #Player and Monster have Sufficent HP
        else:
            fight_choice = getUserFightOptions(hp, gold, monster_health, name)
            hp, gold, monster_health, fight = fight_attacks(fight_choice, hp, gold, monster_health, monster_power)
    return hp, gold
#Function controlling death during a monster fight
def fight_death(hp, gold, monster_hp, monster_gold):
    """
    Protocols for death during a monster fight.
    
    Parameters:
        hp (float): current health of player.
        gold (int): Current gold balance of player.
        monster_hp (float): current health of monster.
        monster_gold (int): gold of monster being fought
    
    Returns:
        hp (float): health of player
        gold (int): gold balance of player
        
    Examples:
        >>>print(fight_death(0, 15, 25, 26))
        You died! 
        Resetting Health and Gold

        (15, 5)
        
        >>>print(fight_death(25, 16, 0, 27))
        You killed the monster.
        You won 24 Gold from the battle.
        You have gained 25 health from winning
        (50, 40)
    """
    #Death of player
    if hp <= 0:
        print('You died! \nResetting Health and Gold\n')
        hp = 15
        gold = 5
    #Death of Monster
    elif monster_hp <= 0:
        win_gold = random.randint(1, monster_gold)
        print('You killed the monster.')
        print('You won', win_gold, 'Gold from the battle.')
        print('You have gained 25 health from winning')
        gold += win_gold
        hp += 25
    return hp, gold
#Function controlling attacks during monster fight
def fight_attacks(fight_choice, hp, gold, monster_health, monster_power):
    """
    Hold attack options and outcomes for a monster fight.
    
    Parameters:
        fight_choice (int): attack being chosen.
        hp (float): health of player.
        gold (int): gold balance of player.
        monster_health (float): health of monster.
        monster_power (int): power level of monster.
        
    Returns:
        hp (float): updated player health
        gold (int): updated gold balance of player.
        monster_health (float): updated monster health.
        fight (boolean): updated fight status
    
    Examples:
        >>>print(fight_attacks(1, 117, 25, 112, 17))
        Your attack yields 10 damage
        The monster has 102 HP remaining
        The monster did 9 damage, leaving you with 108 HP

        (108, 25, 102, True)
    """
    #Primary Attack
    if fight_choice == 1:
        fight = True
        damage = random.randint(5, 38)
        print(f'Your attack yields {damage} damage')
        monster_health -= damage
        print(f'The monster has {monster_health} HP remaining')
        monster_damage = random.randint(5, monster_power)
        hp -= monster_damage
        print(f'The monster did {monster_damage} damage, leaving you with {hp} HP\n')
    #Shield
    elif fight_choice == 2:
        fight = True
        gold -= 5
        print('5 Gold spent on Shield Potion')
        monster_damage = random.randint(5, monster_power)
        damage = monster_damage /2
        monster_health -= damage
        print(f'The monster did {monster_damage} damage, your shield repeled the damage,'
              f'as a result the monster lost {damage} HP leaving it at {monster_health} HP\n')
    #Run from Fight
    else:
        gold -= 10
        fight = False
    return hp, gold, monster_health, fight    
#Answer Validation function
def validate_answer3(answer):
    """
    Validates answers for 3 point menu.
    
    Parameters:
        answer (str): answer given from function call.
    
    Returns:
        answer (str): returns a validate answer for a three option menu.
    
    Examples:
        >>>print(validate_answer3(5))
        Not acceptable input, please try again
        >>>3
        3
    """  
    #Validates answers for all menus
    while not (answer == '1' or answer == '2' or answer == '3'):
        print ('Not acceptable input, please try again')
        answer = input()
    return int(answer)   
#Checks to ensure sufficent gold
def gold_check(gold, gold_need):
    """
    Ensures sufficent gold balance for purchase.
    
    Parameters:
        gold (int): current gold balance of player.
        gold_need (int): the amount of gold neccessary to complete purchase.
    Returns:
        Value validation: True or False dependent on sufficency
    
    Examples:
        >>>print (gold_check(15, 6))
        True
        
        >>>print (gold_check(5, 10))
        Insufficent Gold, Please choose new option
        False
    """
    if gold_need > gold:
        print('Insufficent Gold, Please choose new option')
        return False
    else:
        return True
#Ensures gold isnt below zero
def final_gold(gold):
    """
    Ensures final gold level cannot be below 0.
    
    Parameters:
        gold (int): current gold balance of player
    
    Returns:
        gold (int): non-negative gold balance of player
    
    Examples:
        >>>print(final_gold(15)
        15
        
        >>>print(final_gold(-7)
        0
    """
    if gold < 0:
        gold = 0
    return gold
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
    
    #Test Conditions for town_menu function
    print(town_menu(45, 62))
    print(town_menu(5, 17))
    print(town_menu(150, 2.4))
    
    #Test Conditions for displayFightStatistics function
    displayFightStatistics(48, 153, 'Dragon')
    displayFightStatistics(187, 4)
    displayFightStatistics(4, 16)
    
    #Test conditions for validate_answer3 function
    print(validate_answer3('5'))
    print(validate_answer3('1'))
    print(validate_answer3('2'))
    
    #Test conditions for getUserFightOptions
    print(getUserFightOptions(50, 17, 42, 'Goblin'))
    print(getUserFightOptions(19, 125, 42, 'Dragon'))
    print(getUserFightOptions(172, 21, 76, 'Ankle Biter'))
    
    #Test conditions for monster_fight 
    print (monster_fight(400, 17))
    print (monster_fight(25, 127))  

    #Test conditions for gold_check
    print(gold_check(15, 6))
    print(gold_check(5, 10))
    
    #Test conditions for final_gold
    print(final_gold(15))
    print(final_gold(-7))
    
    #Test conditions for fight_death:
    print(fight_death(0, 15, 25, 26))
    print(fight_death(25, 16, 0, 27))
    
    #Test conditions for fight_attacks:
    print(fight_attacks(1, 117, 25, 112, 17))
    print(fight_attacks(3, 117, 32, 112, 17))
if __name__ == "__main__":
    test_functions()
