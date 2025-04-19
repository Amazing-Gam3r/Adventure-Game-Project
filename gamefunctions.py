"""Contains operational functions for execution and playability in an adventure game.

This module contains the functions: 
gamestart():
loadgame_start():
gamesave(hp, gold, inv, town_x, town_y):
mapUsage(hp, gold, inventory, town_x, town_y, player_x, player_y):
purchase_item(itemPrice, startingMoney, quantity = 1):
print_welcome(name, width = 20):
item_shop(gold, inventory):
print_shop_menu(item1Name, item1Price, item2Name, item2Price, item3Name, item3Price, item4Name, item4Price):
town_menu(hp, gold):
displayFightStatistics(user_hp, monster_hp, monster_name = 'Monster'):
getUserFightOptions(user_hp, gold, monster_hp, monster_name):
monster_fight(hp, gold, inventory):
fight_death(hp, gold, monster_hp, monster_gold):
fight_attacks(fight_choice, hp, gold, monster_health, monster_power, inventory):
fight_inventory(hp, monster_health, monster_power, inventory):
validate_answer4(answer):
validate_answer3(answer):
gold_check(gold, gold_need):
final_gold(gold):
test_functions():
these functions comprise what is required to create an adventure game.
"""

#gamefunctions.py
#Tucker Werhane
#April 13th, 2025
#This program holds all functions needed to run and play an adventure game

#Imports needed modules
import random #genertaes random numbers
import os #allows for system data retrivial
import sys
import json #allows for saving and laoding of json files
import pygame_system #operates pygame to create a map
import wanderingMonster

#Starts game with base needed data
def gamestart():
    """
    Intiates the adventure game with either default settings or a previously saved game.
    
    Parameters:
        None
        
    Returns:
        player_hp (float): health of player.
        player_gold (int): gold balance of player.
        player_inventory (list): Current inventory of player
        town_x (int): x coordinate of town
        town_y (int): y coordinate of town
        play_game (bool): if game loop wil run after gamestart complete
        
    Examples:
        >>>print(gamestart())
        Welcome to an Adventure Game!
        Please choose how to continue:
        1) New Game
        2) Load Existing Game
        3) Quit Now
        >>>2
        What is the name of your save file?
        (Don't include the '.json'):
        >>>test11
        Enter Player Name:
        >>>Tucker
           Hello, Tucker!   
        (172.0, 12, [])
    """
    print('Welcome to an Adventure Game!') #Prints game title welcome 
    #Prints and collect menu choice
    print('Please choose how to continue:')
    user_choice = input('1) New Game\n'
                        '2) Load Existing Game\n'
                        '3) Quit Now\n')
    user_choice = validate_answer3(user_choice) #validate users choice
    
    if user_choice != 3: #if game is to be played
        play_game = True #sets play of game to true
        if user_choice == 1: #Creates player stats from baseline
            player_hp = 250
            player_gold = 100
            player_inventory = []
            #establishes town location not on border of map
            town_x = random.randint(1,8) * 32
            town_y = random.randint(1,8) * 32
        elif user_choice == 2: #loads player stats from save file
            player_hp, player_gold, player_inventory, town_x, town_y = loadgame_start()
        
        #prints player welcome
        print_welcome (input('Enter Player Name:\n'))
        
    #game not to be played sets all values to zero and sets game play to false   
    elif user_choice == 3:
        player_hp = 0
        player_gold = 0
        player_inventory = []
        town_x = 0
        town_y = 0
        print("Please come again")
        play_game = False

    #establishs monster locations
    monster1, monster2 = wanderingMonster.monster_creation(town_x, town_y)
    return player_hp, player_gold, player_inventory, town_x, town_y, play_game, monster1, monster2

#Loads player stats from save file
def loadgame_start():
    """
    Loads a game file from memory and outputs data from file.
    
    Parameters:
        None
    
    Returns:
        player_hp (float): player health pulled from save file
        player_gold (int): player gold pulled from save file
        player_inventory (list): players inventory pulled from save file
        town_x (int): x coordinate of town pulled from save file
        town_x (int): y coordinate of town pulled from save file
    
    Examples:
        >>>print(loadgame_start())
        What is the name of your save file?
        (Don't include the '.json'):
        >>>test11
        (172.0, 12, [])
    """
    file_name = input("What is the name of your save file?\n(Don't include the '.json'):\n") # Collects save file name
    file_name = str(file_name + '.json') #adds file extension to save name
    file_good = False #sets loop confirming valid name to false
    while file_good == False:
        if os.path.isfile(file_name) == True: #checks to make sure file name is valid
            file_good = True #When file name is valid exits while loop
        else: #if file is invalid prompts user to try again
            print('Invalid Filename, please try again')
            file_name = input()
            file_name = file_name + '.json'
    #Opens save file        
    with open(file_name, 'r') as game_file:
        data = json.load(game_file)
        #extracts data points from save file
        player_hp = float(data['player_hp'])
        player_gold = int(data['player_gold'])
        player_inventory = data['player_inventory']
        town_x = int(data['town_x'])
        town_y = int(data['town_y'])
    return player_hp, player_gold, player_inventory, town_x, town_y

#Saves game data to .json file
def gamesave(hp, gold, inv, town_x, town_y):
    """
    Saves the game file.
    
    Parameters:
        hp (float): player health at point of save.
        gold (int): player gold balance when saved.
        inv (list): current player inventory
        town_x (int): x coordinate of town
        town_y (int): y coordinate of town
    
    Returns:
        Saved File
    
    Examples:
        >>>gamesave(172, 12, [])
        What would you like to call your save?
        >>>test11
        Game Over (Data Saved)!
        Final Health was: 172.
        Final Gold was: 12.
    """    
    save_name = input('What would you like to call your save?\n') #Collects name for save file
    save_name = save_name + '.json' #adds .json file extension to file name
    with open(save_name, 'w') as game_files: #Creates and saves new file
        #estbalishes data for json
        hp = str(hp)
        gold = str(gold)
        town_x = str(town_x)
        town_y = str(town_y)
        game_data = {'player_hp' : hp, 'player_gold' : gold, 'player_inventory' : inv, 'town_x' : town_x, 'town_y' : town_y}
        json.dump(game_data, game_files, indent=2)
    #prints game ending message
    print('Game Over (Data Saved)!')
    print(f'Final Health was: {hp}.\nFinal Gold was: {final_gold(int(gold))}.')

#Creates and utilizes game map    
def mapUsage(hp, gold, inventory, town_x, town_y, player_x, player_y, monster1, monster2):
    """
    Creates map using pygame_system module.
    
    Parameters:
        hp (float): player health.
        gold (int): player gold balance.
        inventory (list): current player inventory.
        town_x (int): x coordinate of town.
        town_y (int): y coordinate of town.
        player_x (int): x coordinate of player.
        player_y (int): y coordinate of player.
    
    Returns:
        hp (float): player health.
        gold (int): player gold balance.
        play_game (bool): whether game will continue
     
    Examples:
        >>>mapUsage(120, 14, [], 92, 128, 32, 32)
    """
    #Creates pygame screen and map   
    (player_x, player_y, town_yes,
     monster_yes, monster_1, monster_2) = pygame_system.make_map(town_x, town_y, player_x, player_y, monster1, monster2)
    play_game = True
    if town_yes == True: #If player ended map on the town
        pass
    elif monster_yes == True: #if player ended map on a monster
        if monster_1 == True:
            hp, gold, inventory, monster1, monster_death = monster_fight(hp, gold, inventory, monster1)
            if monster_death == True:
                monster1.death()
        elif monster_2 == True:
            hp, gold, inventory, monster2, monster_death = monster_fight(hp, gold, inventory, monster2)
            if monster_death == True:
                monster2.death()
        hp, gold, inventory, play_game, monster1, monster2 = mapUsage(hp, gold, inventory, town_x,
                                                                      town_y, player_x, player_y, monster1, monster2)
    else: #If player force quit map
        play_game = False
    monster1.move()
    monster2.move()
    monster1, monster2 = monster_death_check(monster1, monster2, town_x, town_y)
    return hp, gold, inventory, play_game, monster1, monster2

#defines check function to ensure proper number of monsters
def monster_death_check(monster1, monster2, town_x, town_y):
    if monster1.alive == False and monster2.alive == False:
        monster1, monster2 = wanderingMonster.monster_creation(town_x, town_y)
    return monster1, monster2
#Defines purchase_item function
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

#A function that a prints welcome sign 
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

#item shop function
def item_shop(gold, inventory):
    """
    Allows player to purchase items to add to their inventory.
    
    Parameters:
        gold (int): balance of players gold.
        inventory (list): current items in the players inventory.
    
    Returns:
        gold (int): balance of players gold.
        inventory (list): current items in the players inventory.
    
    Examples:
        >>>print(item_shop(73, []))
        Welcome to the Item Shop
        You currently have a balance of 73 gold.

        /-----------------------------------\
        | 1) Star Sword              $42.00 |
        | 2) Instant Kill Potion     $81.00 |
        | 3) Smiley Emoji             $2.00 |
        | 4) Exit                     $0.00 |
        \-----------------------------------/
        What would you like to buy?
        >>>1
        You have purchased Star Sword for 42 gold.

        Current gold balance now: 31
        Current Inventory
        [{'name': 'Star Sword', 'type': 'weapon', 'Durability': 45}]
    """    
    #Prints welcoming info
    print('Welcome to the Item Shop')
    print('You currently have a balance of', gold, 'gold.\n')
    #estbalishes descriptions of items 
    Sword = {"name" : "Star Sword", "type" : "weapon", "Durability" : 45}
    Potion = {"name" : "Instant Kill Potion", "type" : "potion", "Durability" : 1}
    Emoji = {"name" : "Smiley Emoji", "type" : "emoji", "Durability" : 10000}
    print_shop_menu("Star Sword", 42, "Instant Kill Potion", 81, "Smiley Emoji", 2, "Exit" , 0)
    shopping = True
    while shopping == True: #Shopping loop
        choice = input('What would you like to buy?\n')
        valid_choice = validate_answer4(choice)
        items = [Sword, Potion, Emoji]
        shopping = True
        if valid_choice == 4: #Exits shop
            shopping = False
            print('Exiting Shop')
        else:
            if items[valid_choice - 1] in inventory: #Checks to see if player already has item
                print('Item already in inventory')
            elif valid_choice == 1: #purchases item (removes gold from balance and adds item to inventory)
                if gold_check(gold, 42) == True: #purchases sword
                    print(f'You have purchased {items[valid_choice - 1]['name']} for 42 gold.\n')
                    gold -= 42
                    print(f'Current gold balance now: {gold}')
                    inventory.append(items[valid_choice - 1])
                    print('Current Inventory')
                    print(inventory)
            elif valid_choice == 2: #purchases potion
                if gold_check(gold, 81) == True:
                    print(f'You have purchased {items[valid_choice - 1]['name']} for 81 gold.\n')
                    gold -= 81
                    print(f'Current gold balance now: {gold}')
                    inventory.append(items[valid_choice - 1])
                    print('Current Inventory')
                    print(inventory)   
            elif valid_choice == 3: #purchases smiley face
                if gold_check(gold, 2) == True:
                    print(f'You have purchased {items[valid_choice - 1]['name']} for 2 gold.\n')
                    gold -= 2
                    print(f'Current gold balance now: {gold}')
                    inventory.append(items[valid_choice - 1])
                    print('Current Inventory')
                    print(inventory)
    return gold, inventory

#prints a shop menu
def print_shop_menu(item1Name, item1Price, item2Name, item2Price, item3Name, item3Price, item4Name, item4Price):
    """
    Prints a shop menu given two items and their prices.

    Parameters:
        item1Name (str): Name of first item to be presented in the shop.
        item1Price (int): Price of first item.
        item2Name (str): Name of second item presented in shop.
        item2Price (int): Price of second item.
        item3Name (str): Name of third item presented in shop.
        item3Price (int): Price of third item.
        item4Name (str): Name of fourth item presented in shop.
        item4Price (int): Price of fourth item.
    
    Returns:
        None
    
    Prints:
        Shop Menu: a table with two items and their prices.
    
    Examples:
        >>>print_shop_menu ("Sword", 57.72, "Heal Potion", 78, 'Grapes', 18, 'Rock', 19)
        /-------------------------\
        | 1) Sword            $58 |
        | 2) Heal Potion      $78 |
        | 3) Grapes           $18 |
        | 4) Rock             $19 |
        \-------------------------/
    """
    #formats item lisitngs
    item1Price = (f'{int(item1Price):.2f}')
    item2Price = (f'{int(item2Price):.2f}')
    item3Price = (f'{int(item3Price):.2f}')
    item4Price = (f'{int(item4Price):.2f}')
    #formats maneu design
    top_string = '/' + ('-' * 35) +'\\'
    bottom_string = '\\' + ('-' * 35) +'/'
    #prints menu
    print (top_string)
    print(f'| 1) {item1Name:<22}{('$' + item1Price):>8} |')
    print(f'| 2) {item2Name:<22}{('$' + item2Price):>8} |')
    print(f'| 3) {item3Name:<22}{('$' + item3Price):>8} |')
    print(f'| 4) {item4Name:<22}{('$' + item4Price):>8} |')
    print (bottom_string)

#main game menu
def town_menu(hp, gold):
    """
    Prints a initial menu for actions to be taken within the game.
    
    Parameters:
        hp (int): The amount of health the player currently has.
        gold (float): The current amount of gold the player has.
    Returns:
        user_choice: A value of 1, 2, 3, or 4 that corresponds to a specific action set.
    
    Prints:
        Town menu: prints a list of possible actions taken
    
    Examples:
        >>>print(town_menu(45, 62))
        You are in town.
        Current HP: 45, Current Gold: 62
        What would you like to do?
        1) Enter Map (Green = Town | Everything Else = Monster)
        2) Sleep (Restore HP for 15 Gold)
        3) Shop
        4) Quit
    """
    #Prints options and welcome
    print ('You are in town.')
    print (f'Current HP: {hp}, Current Gold: {gold}')
    user_choice = input('What would you like to do?\n\n'
                        '1) Enter Map (Green = Town | Everything Else = Monster)\n'
                        '2) Sleep (Restore HP for 10 Gold)\n'
                        '3) Shop\n'
                        '4) Save & Quit\n')
    #validates users choice
    user_choice = validate_answer4(user_choice)
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
        3) Use Inventory item
        4) Leave fight (Lose 1 Gold)
        >>>1
        1
    """
    displayFightStatistics(user_hp, monster_hp, monster_name)
    print (f'(Current Gold: {gold}) \nHow would you like to continue?')
    #Determines players move choice for the fight
    user_choice = input('1) Primary Attack (5-37 damage)\n'
                        '2) Shield Potion (Costs 5 Gold, Monster takes half of attack damage)\n'
                        '3) Use Inventory Item\n'
                        '4) Leave fight (Lose 10 Gold)\n')
    #ensures sufficent funds for shield potion
    sufficency = False
    while sufficency == False:
        user_choice = validate_answer4(user_choice)
        if user_choice == 2:
            sufficency = gold_check(gold, 5)
            if sufficency == False:
                user_choice = input()
        else:
            sufficency = True
    return user_choice

#Fight Sequence Function
def monster_fight(hp, gold, inventory, monster):
    """
    Conducts a fight sequence against a monster.
    
    Parameters:
        hp (int): Current health of player.
        gold (float): Current money held by the player
        inventory (list): current inventory obtained by player
        
    Returns: hp, gold
        hp (int): remaining player health after battle.
        gold (float) remaing gold held by player after battle.
        
    Examples:
        >>>print (monster_fight(400, 17))
        You are fighting An Elf.
        This monster has 120 HP and 95 power.

        ...Fight loop plays multiople times
       
        Fight over
        You killed the monster.
        You won 1 Gold from the battle.
        You have gained 25 health from winning
        (175, 3)
    """
    #Selects random monster
    name = monster.monster['name']
    print(f'You are fighting {name}.')
    #establishes monster qualities
    monster_health = int(monster.monster['health'])
    monster_power = int(monster.monster['power'])
    print(f'This monster has {monster_health} HP and {monster_power} power.\n')
    fight = True
    #fight sequence loop
    while fight == True:
        #Death of monster or player
        if hp <= 0 or monster_health <= 0:
            hp, gold, monster_death = fight_death(hp, gold, monster_health, monster.monster['money'])
            fight = False
        #Player and Monster have Sufficient HP
        else:
            fight_choice = getUserFightOptions(hp, gold, monster_health, name)
            (hp, gold, monster_health,
             fight, inventory) = fight_attacks(fight_choice, hp, gold, monster_health, monster_power, inventory)
            monster_death = False
    return hp, gold, inventory, monster, monster_death

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

        (150, 50)
        
        >>>print(fight_death(25, 16, 0, 27))
        You killed the monster.
        You won 24 Gold from the battle.
        You have gained 25 health from winning
        (50, 40)
    """
    #Death of player
    if hp <= 0:
        #resets player health and gold
        print('You died! \nResetting Health and Gold\n')
        hp = 150
        gold = 50
        monster_death = False
        
    #Death of Monster
    elif monster_hp <= 0:
        win_gold = random.randint(1, int(monster_gold))
        print('You killed the monster.')
        print('You won', win_gold, 'Gold from the battle.')
        print('You have gained 25 health from winning')
        #increases health and gold based from winning battle
        gold += win_gold
        hp += 25
        monster_death = True
    return hp, gold, monster_death

#Function controlling attacks during monster fight
def fight_attacks(fight_choice, hp, gold, monster_health, monster_power, inventory):
    """
    Hold attack options and outcomes for a monster fight.
    
    Parameters:
        fight_choice (int): attack being chosen.
        hp (float): health of player.
        gold (int): gold balance of player.
        monster_health (float): health of monster.
        monster_power (int): power level of monster.
        inventory (list): contents of players inventory
        
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
        
        #randomly generates damage value
        damage = random.randint(5, 38)
        print(f'Your attack yields {damage} damage')
        monster_health -= damage
        print(f'The monster has {monster_health} HP remaining')
        
        #Monster attacks player
        monster_damage = random.randint(5, monster_power)
        hp -= monster_damage
        print(f'The monster did {monster_damage} damage, leaving you with {hp} HP\n')
    
    #Shield
    elif fight_choice == 2:
        fight = True
        gold -= 5
        print('5 Gold spent on Shield Potion')
        #reverses half of monsters damage
        monster_damage = random.randint(5, monster_power)
        damage = monster_damage /2
        monster_health -= damage
        print(f'The monster did {monster_damage} damage, your shield repeled the damage,'
              f'as a result the monster lost {damage} HP leaving it at {monster_health} HP\n')
    
    #Inventory Item
    elif fight_choice == 3:
        fight = True
        hp, monster_health, inventory = fight_inventory(hp, monster_health, monster_power, inventory)
    
    #Run from Fight
    else:
        gold -= 10
        fight = False
        
    return hp, gold, monster_health, fight, inventory

# allows user to use inventory items during fight
def fight_inventory(hp, monster_health, monster_power, inventory):
    """
    Allows use of inventory during fight.
    
    Parameters:
        hp (float): players health
        monster_health (float): monsters health.
        monster_power (int): maximum damage of monster
        inventory (list): current items in players inventory
        
    Returns:
        hp (float): players health
        monster_health (float): monsters health.
        inventory (list): current items in players inventory
    
    Examples:
        >>>print(fight_inventory(175, 118, 65, [{"name" : "Star Sword", "type" : "weapon", "Durability" : 45},
                                               {"name" : "Instant Kill Potion", "type" : "potion", "Durability" : 1},
                                               {"name" : "Smiley Emoji", "type" : "emoji", "Durability" : 10000}]
        Usable inventory
        [{'name': 'Star Sword', 'type': 'weapon', 'Durability': 45}]
        Choose item to use
        1 options:
        >>>1
        You have equiped Star Sword, currently at 45 durability
        Your attack yields 147 damage
        The monster has -29 HP remaining
        The monster did 13 damage, leaving you with 162 HP

        Star Sword has lost 10 durabilty
        (162, -29, [{'name': 'Star Sword', 'type': 'weapon', 'Durability': 35}, 
        {'name': 'Instant Kill Potion', 'type': 'potion', 'Durability': 1}, 
        {'name': 'Smiley Emoji', 'type': 'emoji', 'Durability': 10000}])
    """    
    #creates usable inventory list
    invt = []
    
    #adds usable items to usable inventory
    for i in inventory:
        if i['type'] == ('weapon'):
            invt.append(i)
        elif i['type'] == ('potion'):
            invt.append(i)
    print('Usable inventory')
    print(invt)
    if invt != []: #if there is a usable item then a choice is made between items
        print('Choose item to use')
        item_choice = input(f'{len(invt)} options:\n')
        item = invt[int(item_choice) - 1]
        print(f'You have equiped {item['name']}, currently at {item['Durability']} durability')
        
        if item['type'] == 'weapon': #sword atatck
            #damage value
            damage = random.randint(50, 180)
            print(f'Your attack yields {damage} damage')
            monster_health -= damage
            print(f'The monster has {monster_health} HP remaining')
            #monster attack on player
            monster_damage = random.randint(5, monster_power)
            hp -= monster_damage
            print(f'The monster did {monster_damage} damage, leaving you with {hp} HP\n')
            print(f'{item['name']} has lost 10 durabilty')
            #decreases durability of sword
            item['Durability'] = int(item['Durability']) - 10
            if int(item['Durability']) <=0: #if durability is fully used then item is destoyed
                print(f'{item['name']} destroyed')
                inventory.remove(item)
                
        elif item['type'] == 'potion': #potion attack
            print(f'You have used {item['name']}')
            monster_health = 0
            #removes item after one use
            inventory.remove(item)
            
    else: #if no items in usable then exits to fight options
        print('No usable inventory items')
    return hp, monster_health, inventory
    
#Answer Validation functions
def validate_answer4(answer):
    """
    Validates answers for 4 point menu.
    
    Parameters:
        answer (str): answer given from function call.
    
    Returns:
        answer (str): returns a validate answer for a four option menu.
    
    Examples:
        >>>print(validate_answer3(5))
        Not acceptable input, please try again
        >>>3
        3
    """  
    #Validates answers for menus with 4 options
    while not (answer == '1' or answer == '2' or answer == '3' or answer == '4'):
        print ('Not acceptable input, please try again')
        answer = input()
    return int(answer)  
def validate_answer3(answer):
    """
    Validates answers for 3 point menu.
    
    Parameters:
        answer (str): answer given from function call.
    
    Returns:
        answer (str): returns a validate answer for a four option menu.
    
    Examples:
        >>>print(validate_answer3(5))
        Not acceptable input, please try again
        >>>3
        3
    """  
    #Validates answers for menus with 3 options
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
    #checks gold value needed against avaliable gold
    if gold_need > gold:
        print('Insufficent Gold, Please choose new option')
        return False
    else:
        return True
        
#Ensures final gold isn't below zero
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
    #if gold is less than zero gold is set to zero
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
    
    #Test conditions for print_welcome function using diffrent name lengths and differing field widths
    print_welcome('Jeff')
    print_welcome('Frank')
    print_welcome('Carson')
    
    #Test Conditions for print_shop_menu using varietys of items and prices
    print_shop_menu ("Sword", 57.72, "Heal Potion", 78, "Rock", 18, "Potatoes", 7)
    print_shop_menu ("Battle Axe", 178.525, "Cereal", 2.098766, "Grapes", 16, "Sword", 57.72)
    print_shop_menu ("Potatoes", 7, "Grapes", 14.98, 'Oranges', 13.72, "Battle Axe", 178.525)
    
    #Test Conditions for town_menu function
    print(town_menu(45, 62))
    print(town_menu(5, 17))
    print(town_menu(150, 2.4))
    
    #Test Conditions for displayFightStatistics function
    displayFightStatistics(48, 153, 'Dragon')
    displayFightStatistics(187, 4)
    displayFightStatistics(4, 16)
    
    #Test conditions for validate_answer4 function
    print(validate_answer4('5'))
    print(validate_answer4('1'))
    print(validate_answer4('2'))
    
    #Test conditions for getUserFightOptions
    print(getUserFightOptions(50, 17, 42, 'Goblin'))
    print(getUserFightOptions(19, 125, 42, 'Dragon'))
    print(getUserFightOptions(172, 21, 76, 'Ankle Biter'))
    
    #Test conditions for monster_fight 
    print (monster_fight(400, 17, []))
    print (monster_fight(25, 127, []))  

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
    print(fight_attacks(1, 117, 25, 112, 17, []))
    print(fight_attacks(3, 117, 32, 112, 17, []))
    
    #Test conditions for item_shop:
    print(item_shop(73, []))
    print(item_shop(42, []))
    
    #Test condition for fight_inventory:
    print(fight_inventory(175, 118, 65, [{"name" : "Star Sword", "type" : "weapon", "Durability" : 45},
                                               {"name" : "Instant Kill Potion", "type" : "potion", "Durability" : 1},
                                               {"name" : "Smiley Emoji", "type" : "emoji", "Durability" : 10000}]))
                                               
    #Test Condition for load game_start:
    print(loadgame_start())
    
    #Test condition for gamesave:
    gamesave(172, 12, [])
    
    #Test Condition for gamestart:
    print(gamestart())
    
    #test condition for mapUsage:
    print(mapUsage(120, 14, [], 92, 128, 32, 32))

#Runs test_functions if module run directly    
if __name__ == "__main__":
    player_inventory = []
    test_functions()
