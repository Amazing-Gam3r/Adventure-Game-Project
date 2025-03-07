"""Contains an adventure game.

References gamefunctions for operational usage of game.
"""

#game.py
#Tucker Werhane
#March 7th, 2025
#This programs tests two functions, purchase_item and new_random_monster.
#These functions can be called upon anywhere within the script to execute their predetrmined actions.

#Imports gamefunctions, a file containing the neccessary functions for gameplay.
import gamefunctions

#Test cases for importing functions:

#Test conditions for purchase_item function
print('\nTesting purchase_item function\n')
num_purchased, leftover_money = gamefunctions.purchase_item(float(input('Enter item price:\n')), 
                                                            float(input('Enter current balance:\n')), 
                                                            int(input('Enter quantity:\n')))
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

num_purchased, leftover_money = gamefunctions.purchase_item(float(input('Enter item price:\n')), 
                                                            float(input('Enter current balance:\n')), 
                                                            int(input('Enter quantity:\n')))
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

num_purchased, leftover_money = gamefunctions.purchase_item(float(input('Enter item price:\n')), 
                                                            float(input('Enter current balance:\n')), 
                                                            int(input('Enter quantity:\n')))
print (num_purchased, 'items purchased.')
print (leftover_money, 'money remaining.')

# test conditions for new_random_monster function
print ('\nTesting new_random_monster function\n')
my_monster = gamefunctions.new_random_monster()
print (my_monster['name'])
print (my_monster['description'])

my_monster = gamefunctions.new_random_monster()
print (my_monster['name'])
print (my_monster['money'])

my_monster = gamefunctions.new_random_monster()
print (my_monster['name'])
print (my_monster['health'])
print (my_monster['power'])

#Test conditions for print_welcome function using diffrent name lengths and differing field widths
print ('\nTesting print_welcome function\n')
gamefunctions.print_welcome(str(input('Enter name: \n')))
gamefunctions.print_welcome(str(input('Enter name: \n')))
gamefunctions.print_welcome(str(input('Enter name: \n')))

#Test Conditions for print_shop_menu using varietys of items and prices
print ('\nTesting print_shop_menu function\n')
gamefunctions.print_shop_menu (str(input('Enter item 1 name: \n')), float(input('Enter item 1 price: \n')), 
                               str(input('Enter item 2 name: \n')), float(input('Enter item 2 price: \n')))
gamefunctions.print_shop_menu (str(input('Enter item 1 name: \n')), float(input('Enter item 1 price: \n')), 
                               str(input('Enter item 2 name: \n')), float(input('Enter item 2 price: \n')))
gamefunctions.print_shop_menu (str(input('Enter item 1 name: \n')), float(input('Enter item 1 price: \n')), 
                               str(input('Enter item 2 name: \n')), float(input('Enter item 2 price: \n')))
