"""Contains an adventure game.

References gamefunctions for operational usage of game.
Establishes initial player stats prior to running the main game loop.
"""

#game.py
#Tucker Werhane
#April 13th, 2025
#This programs runs an adventure game that uses and creates save files
#During the game, the player can shop in town or leave town to fight monsters

#Imports gamefunctions, a module containing the neccessary functions for gameplay.
import gamefunctions

#Calls gamestart function which either creates a new set of base values or pulls them from a save file
player_hp, player_gold, player_inventory, town_x, town_y, play_game, monster1, monster2 = gamefunctions.gamestart()

#Main Game Loop
while play_game == True:
    move = gamefunctions.town_menu(player_hp, player_gold) #Gets player move
    # If player move is one then the player is sent to the map (If map is closed abruptly then the game loop shuts off)
    if move == 1:
        (player_hp, player_gold, player_inventory,
         play_game, monster1, monster2) = gamefunctions.mapUsage(player_hp, player_gold,
                                                                 player_inventory, town_x, town_y,
                                                                 town_x, town_y, monster1, monster2)
    elif move == 2: # If player move is two then they sleep and gain health
        print('You Slept')
        player_hp = 250
        player_gold -= 10
    elif move == 3: #if player move is three then they go to the shop
        gold, player_inventory = gamefunctions.item_shop(player_gold, player_inventory)
    elif move == 4: # If player move is four they are prompted to save the game and the game loop is shut off
        gamefunctions.gamesave(player_hp, player_gold, player_inventory, town_x, town_y)
        play_game = False
