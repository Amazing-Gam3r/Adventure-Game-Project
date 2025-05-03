"""Contains the componets required to create and trade with a wandering trader NPC for an adventure game.

This module contains the classes:
    WanderingTrader(town_x, town_y): used to generate and trade with a Trader NPC.

This class allows for interaction and generation of a Trading NPC.
"""

#wanderingTrader.py
#Tucker Werhane
#May 4th, 2025
#This module generates a trading NPC

import random #used for random trade avaliabilties
import gamefunctions #used to create shop table and check inputs.

class WanderingTrader:
    """WanderingTrader class to generate and trade with a Trader NPC.

        Instance Objects:
            x (int): x coordinate of the monster in the class instance.
            y (int): y coordinate of the monster in the class instance.
            town_x (int): x coordinate of the town in the class instance.
            town_y (int): y coordinate of the town in the class instance.
            image (str): the path to the image of the wandering trader NPC.
            traded (bool) whether the monster has been traded with.

        Methods:
            create_trader(): establishes location of the wandering trader NPC.
            trader_shop(): randomizes chances of items trader carries.
            trader_purchase(): allows player to purchase an item from the wandering trader NPC.
            monsters_killed(): updates trader qualties for after both monsters are killed.
            """

    def __init__(self, town_x, town_y):
        """
        Defines intial charecteristics of WanderingTrader class.

        Parameters:
            town_x (int): x coordinate of the town in the class instance.
            town_y (int): y coordinate of the town in the class instance.

        Example:
            >>trader = WanderingTrader(64, 128)
            >>print(trader.image)
            images/WanderingTrader.png
        """
        self.x = 0
        self.y = 0
        self.town_x = town_x
        self.town_y = town_y
        self.image = 'images/WanderingTrader.png'
        self.traded = False #NPC has not been interacted with as default

    def create_trader(self):
        """
        Randomly chooses location for the wandering trader NPC.

        Examples:
            >>WanderingTrader.create_trader()
        """
        #Randomly selects location of trader NPC
        self.x = random.randint(0, 9) * 32
        self.y = random.randint(0, 9) * 32
        #Ensures NPC is in different location then town
        while self.x == self.town_x and self.y == self.town_y:
            self.x = random.randint(0, 9) * 32
            self.y = random.randint(0, 9) * 32

    def trader_shop(self):
        """
        Randomly selects trade options for the Trader NPC.

        Returns:
            trades (bool): whether a trade is possible.
            items (list): the list of possible trade items and their prices.

        Examples:
            >>print(WanderingTrader.trader_shop())
            No Trades Available Today
            False, []
        """

        #Special items sold by the wandering trader.
        special_items =[{"name" : "Jaeger Sword", "type" : "weapon", "power" : 170, "Durability" : 60}, #0
                        {"name" : "Dual Daggers", "type" : "weapon", "power" : 60, "Durability" : 70}, #1
                        {"name" : "Otachi", "type" : "weapon", "power" : 180, "Durability" : 100}, #2
                        {"name" : "Hades Breath", "type" : "potion", "Durability" : 1}, #3
                        {"name" : "Hades Staff", "type" : "weapon", "power" : 200, "Durability" : 1000}, #4
                        {"name" : "Jousting Rod", "type" : "weapon", "power" : 25, "Durability" : 25}, #5
                        {"name" : "Wooden Sword", "type" : "weapon", "power" : 15, "Durability" : 15}, #6
                        {"name" : "Plasma Rifle", "type" : "weapon", "power" : 250, "Durability" : 200}, #7
                        {"name" : "Sun Sword", "type" : "weapon", "power" : 130, "Durability" : 30}] #8
        #gets random number with 100 possibilties
        chance_num = random.randint(0,100)
        # 60% chance of no trade avaliable
        if 0 <= chance_num <= 60:
            print('No Trades Available Today')
            trades = False
            items = []
        else: # 40% trade is avaliable
            trades = True
            if 61 <= chance_num <= 90: # 30% bad trade possiblties
                gamefunctions.print_shop_menu(special_items[3]['name'], 30,
                                              special_items[5]['name'], 25,
                                              special_items[1]['name'], 45,
                                              "Exit", 0)
                items = [[special_items[3], 30], [special_items[5], 25], [special_items[1], 45]]
            elif 91 <= chance_num < 100: # 9% decent trade possibilties
                gamefunctions.print_shop_menu(special_items[6]['name'], 15,
                                              special_items[8]['name'], 60,
                                              special_items[0]['name'], 110,
                                              "Exit", 0)
                items = [[special_items[6], 15], [special_items[8], 60], [special_items[0], 110]]
            elif chance_num == 100: # 1% chance great trade possibilties
                gamefunctions.print_shop_menu(special_items[2]['name'], 160,
                                              special_items[4]['name'], 300,
                                              special_items[7]['name'], 300,
                                              "Exit", 0)
                items = [[special_items[2], 160], [special_items[4], 300], [special_items[7], 300]]
        return trades, items

    def trader_purchase(self, invt, gold):
        """
        Allows player to purchase an item from the wandering trader NPC.

        Parameters:
            invt (list): the list of items the player has in their inventory.
            gold (int): the balance of gold reatined by the player.

        Returns:
            invt (list): the updated list of items the player has in their inventory.
            gold (int): the updated balance of gold reatined by the player.

        Examples:
            >>WanderingTrader.trader_purchase([], 2000)
            Welcome to the Wandering Trader
            At the Wandering Trader you may only buy one item!
            Choose Wisely!
            You currently have a balance of 2000 gold.

            No Trades Available Today
        """

        # Prints welcoming info
        print('Welcome to the Wandering Trader')
        self.traded = True # changes interaction status
        print('At the Wandering Trader you may only buy one item!')
        print('Choose Wisely!')
        print('You currently have a balance of', gold, 'gold.\n')
        #gets trade options and presents shop table
        trade_yes, available_items = self.trader_shop()
        if trade_yes:
            print ('What would you like to buy?')
            #gets purchase choice from user
            purchase_choice = input('Item #> ')
            #validates users input
            purchase_choice = gamefunctions.validate_answer4(purchase_choice)
            if purchase_choice == 4: #Player chose to exit shop
                print('You may regret giving up this opportunity.')
                print('Leaving Trader')
            else: #player bought something from shop
                if available_items[purchase_choice - 1][0] in invt:  # Checks to see if player already has item
                    print('Item already in inventory')
                else: # purchases item (removes gold from balance and adds item to inventory)
                    if gamefunctions.gold_check(gold, available_items[0][1]):  # ensures sufficent gold
                        print(f'You have purchased {available_items[purchase_choice - 1][0]['name']} for '
                              f'{available_items[purchase_choice - 1][1]} gold.\n')
                        gold -= available_items[purchase_choice - 1][1]
                        print(f'Current gold balance now: {gold}')
                        invt.append(available_items[purchase_choice - 1][0])
                        print('Current Inventory')
                        print(invt)
        return invt, gold

    def monsters_killed(self):
        """
        Updates trader status based on if monsters have been killed.

        Examples:
            >>WanderingTrader.monsters_killed()
        """
        self.create_trader() #generates new coordinates for the trader NPC
        self.traded = False #resets interaction status

if __name__ == '__main__':
    test_instance = WanderingTrader(64, 128)
    test_instance.trader_shop()
    test_instance.trader_purchase([], 2000)
    test_instance.monsters_killed()