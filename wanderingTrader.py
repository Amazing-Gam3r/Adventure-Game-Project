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
from gamefunctions import print_shop_menu, validate_answer4, gold_check #used to create shop table and check inputs.

class WanderingTrader:
    def __init__(self, town_x, town_y):
        self.x = 0
        self.y = 0
        self.town_x = town_x
        self.town_y = town_y
        self.image = 'images/WanderingTrader.png'
        self.traded = False
    def create_trader(self):
        self.x = random.randint(0, 9) * 32
        self.y = random.randint(0, 9) * 32
        while self.x == self.town_x and self.y == self.town_y:
            self.x = random.randint(0, 9) * 32
            self.y = random.randint(0, 9) * 32
    def trader_shop(self):
        special_items =[{"name" : "Jaeger Sword", "type" : "weapon", "power" : 170, "Durability" : 60}, #0
                        {"name" : "Dual Daggers", "type" : "weapon", "power" : 60, "Durability" : 70}, #1
                        {"name" : "Otachi", "type" : "weapon", "power" : 180, "Durability" : 100}, #2
                        {"name" : "Hades Breath", "type" : "potion", "Durability" : 1}, #3
                        {"name" : "Hades Staff", "type" : "weapon", "power" : 200, "Durability" : 1000}, #4
                        {"name" : "Jousting Rod", "type" : "weapon", "power" : 25, "Durability" : 25}, #5
                        {"name" : "Wooden Sword", "type" : "weapon", "power" : 5, "Durability" : 15}, #6
                        {"name" : "Plasma Rifle", "type" : "weapon", "power" : 250, "Durability" : 200}, #7
                        {"name" : "Sun Sword", "type" : "weapon", "power" : 130, "Durability" : 30}] #8
        chance_num = random.randint(0,100)
        if 0 <= chance_num <= 60:
            print('No Trades Available Today')
            trades = False
            items = []
        else:
            trades = True
            if 61 <= chance_num <= 90:
                print_shop_menu(special_items[3]['name'], 30,
                                              special_items[5]['name'], 25,
                                              special_items[1]['name'], 45,
                                              "Exit", 0)
                items = [[special_items[3], 30], [special_items[5], 25], [special_items[1], 45]]
            elif 91 <= chance_num < 100:
                print_shop_menu(special_items[6]['name'], 15,
                                              special_items[8]['name'], 60,
                                              special_items[0]['name'], 110,
                                              "Exit", 0)
                items = [[special_items[6], 15], [special_items[8], 60], [special_items[0], 110]]
            elif chance_num == 100:
                print_shop_menu(special_items[2]['name'], 160,
                                              special_items[4]['name'], 300,
                                              special_items[7]['name'], 300,
                                              "Exit", 0)
                items = [[special_items[2], 160], [special_items[4], 300], [special_items[7], 300]]
        return trades, items
    def trader_purchase(self, invt, gold):
        # Prints welcoming info
        print('Welcome to the Wandering Trader')
        self.traded = True
        print('At the Wandering Trader you may only buy one item!')
        print('Choose Wisely!')
        print('You currently have a balance of', gold, 'gold.\n')
        trade_yes, available_items = self.trader_shop()
        if trade_yes:
            print ('What would you like to buy?')
            purchase_choice = input('Item #> ')
            purchase_choice = validate_answer4(purchase_choice)
            if purchase_choice == 4:
                print('You may regret giving up this opportunity.')
                print('Leaving Trader')
            else:
                if available_items[purchase_choice - 1][0] in invt:  # Checks to see if player already has item
                    print('Item already in inventory')
                else: # purchases item (removes gold from balance and adds item to inventory)
                    if gold_check(gold, available_items[0][1]):  # ensures sufficent gold
                        print(f'You have purchased {available_items[purchase_choice - 1][0]['name']} for '
                              f'{available_items[purchase_choice - 1][1]} gold.\n')
                        gold -= available_items[purchase_choice - 1][1]
                        print(f'Current gold balance now: {gold}')
                        invt.append(available_items[purchase_choice - 1][0])
                        print('Current Inventory')
                        print(invt)
        return invt, gold
    def monsters_killed(self):
        self.create_trader()
        self.traded = False
if __name__ == '__main__':
    test_instance = WanderingTrader(64, 128)
    test_instance.trader_shop()
    test_instance.trader_purchase([], 2000)
    test_instance.monsters_killed()