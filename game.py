"""Contains an adventure game.

References gamefunctions for operational usage of game.
Establishes initial player stats prior to running the main game loop.
"""

#game.py
#Tucker Werhane
#March 8th, 2025
#This programs tests two functions, purchase_item and new_random_monster.
#These functions can be called upon anywhere within the script to execute their predetrmined actions.

#Imports gamefunctions, a file containing the neccessary functions for gameplay.
import gamefunctions

#Initial Player Stats for in Game use
player_hp = 250
player_gold = 15
play_game = True
gamefunctions.print_welcome (input('Enter Player Name:\n'))

#Main Game Loop
while play_game == True:
    move = gamefunctions.town_menu(player_hp, player_gold)
    if move == 1:
        player_hp, player_gold = gamefunctions.monster_fight(player_hp, player_gold)
    elif move == 2:
        print('You Slept')
        player_hp = 250
        player_gold -= 10
    elif move ==3:
        print('Game Over!')
        print(f'Final Health was: {player_hp}.\nFinal Gold was: {player_gold}.')
        play_game = False


