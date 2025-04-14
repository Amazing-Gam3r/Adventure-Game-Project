"""Contains the functions needed to launch an operate a map screen.

 This module contains the function:
    make_map(town_x, town_y, start_x, start_y)
 
 This module also contains the classes:
    Player: used for items involving the player in the map
    MapCreate: used to create map objects
 
 Combined these functions and classes can be used to produce a intercative map for an adventure game.
 """

#pygame_system.py
#Tucker Werhane
#April 13th, 2025
#This module uses pygame to create a interactive map screen for an adventure game

#Imports needed modules for code function
import pygame #Drawing and Screen functions
import time #Allows time dealy to be used in programming
import random # used to generate random numbers

#Player class for plpayer operations
class Player:
    """
    Player class deals with functions and data related to the player.
    
    Objects:
        player_size (int): fixed value fo side length of player square.
        player_color (color): fixed color representing the player.
        
    Initial Objects:
        player_x (int): x position of player
        player_y (int): y position of player
        
    Methods:
        draw_player(surface): draws the player rectangle on the specified surface.
    """
    player_size = 32 #side length of player box
    player_color = (255, 215, 0) # Color of player box
    
    #Intializing class data
    def __init__(self, start_x, start_y):
        """
        Intializes Player class with player_x and player_y.
        
        Parameters:
            start_x (int): x coordinate of where the player is starting
            start_y (int): y coordinate of where the player is starting
        
        Example:
            >>>player1 = Player(0, 0)
        """
        #intially sets values to inputted starts
        self.player_x = start_x
        self.player_y = start_y
    #Draws player 
    def draw_player(self, surface):
        """
        Draws the player rectangle on the specified surface.
        
        Parameters:
            surface: surface player to be drawn onto
        
        Example:
            >>>draw_player(screen)
        """
        #establishes player rectangle
        player = pygame.Rect(self.player_x, self.player_y, self.player_size, self.player_size)
        #draws player rectangle
        pygame.draw.rect(surface, self.player_color, player)

#  MapCreate class for map objects      
class MapCreate:
    """
    Draws important characteristics onto map.
    
    Objects:
        None
        
    Methods:
        drawlines(surface): creates map grid structure
        drawtown(town_x, town_y, surface): creates the circle for town location
        drawmonster (monster_x, monster_y, surface): draws the circle for the monster location
    """
    #Draws map grid lines
    def drawlines(self, surface):
        """
        Draws map grid lines.
        
        Parameters:
            surface: the surface to draw the lines on.
        
        Example:
            >>>drawlines(screen)
        """
        #Line settings
        line_color = (100, 100, 100) #Line Color
        
        #Setup for Vertical Lines
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 320
        for i in range(0, 10):
            pygame.draw.line(surface, line_color, (start_x, start_y), (end_x, end_y))
            
            #Increments lines by 32 pixels along horixontal axis
            start_x += 32
            end_x += 32
        
        #Setup for Horizontal Lines
        start_x = 0
        start_y = 0
        end_x = 320
        end_y = 0
        for i in range(0, 10):
            pygame.draw.line(surface, line_color, (start_x, start_y), (end_x, end_y))
            
            #Increments lines by 32 pixels along vertical axis
            start_y += 32
            end_y += 32
    
    #Draws town circle
    def drawtown(self, town_x, town_y, surface):
        """
        Draws town circle.
        
        Parameters:
            town_x (int) = x coordinate for where the town will be placed.
            town_y (int) = y coordinate for where the town will be placed.
            surface: what surface should the town be drawn on.
        
        Examples:
            >>>drawtown(32, 32, screen)
        """
        #increments town coordinates to land in the center of the grid square
        town_x += 16
        town_y += 16
        town_color = (0, 255, 0) #Town circle color
        town_radius = 12 # Radius of town Circle
        #Draws town circle
        pygame.draw.circle(surface, town_color, (town_x, town_y), town_radius)
    
    #Draws Monster circle    
    def drawmonster(self, monster_x, monster_y, surface):
        """
        Draws the monster circle.
        
        Parameters:
            monster_x (int): x coordinate of monster
            monster_y (int): y coordinate of monster
            surface: surface the monster circle will be drawn on
        
        Examples:
            >>>drawmonster(96, 96, screen)
        """
        #increments monster coordinates to land in the center of the grid square
        monster_x += 16
        monster_y += 16
        monster_color = (255, 0, 0) #Monster Circle Color
        monster_radius = 10 # Radius of monster circle
        #draws monster circle
        pygame.draw.circle(surface, monster_color, (monster_x, monster_y), monster_radius)

#Function running pygame screen
def make_map(town_x, town_y, start_x, start_y):
    """
    Creates a pygame screen depicting a player map.
    
    Parameters:
        town_x (int): X coordinate of where town will be drawn.
        town_y (int): Y coordinate of where town will be drawn.
        start_x (int): X coordinate of where the player currently is.
        start_y (int): Y coordinate of where the player currently is.
    
    Returns:
        player_x (int): ending x coordinate of player.
        player_y (int): ending y coordinate of player.
        town_menu (bool): Status of: if player exited map to town.
        monster_menu (bool): Status of: if player exited map to monster fight.
    
    Examples:
        >>>print(make_map(32, 32, 32, 32))
        (32, 32, True, False)
    """
    #Starts pygame instance
    pygame.init()
    
    #Establishes screen size for the map
    SCREEN_WIDTH = 320
    SCREEN_HEIGHT = 320
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Creates pygame screen
    
    #Initializes function data
    map1 = MapCreate() #Initializes MapCreate class
    player1 = Player(start_x, start_y) #initializes Player class with starting coordinates
    running = True #Sets map run to True
    town_menu = False #Sets output of landed on town to false
    monster_menu = False #Sets output of landed on monster to false
    first_move_done = False #Establishes that first movement on map has not been completed
    
    #Randomly creates coordinate for monster circle
    monster_x = random.randint(0,9) * 32
    monster_y = random.randint(0,9) * 32
    
    #Ensures monster location is not the same as the town location
    while (monster_x == town_x) and (monster_y == town_y):
        monster_x = random.randint(0,9) * 32
        monster_y = random.randint(0,9) * 32
    
    #Main Map Loop
    while running:
        #After the first move is complete each iteration will check to see 
        #if the player has landed on the town space or the monster space
        if first_move_done == True:
            #When Player on Town Space
            if (player1.player_x == town_x) and (player1.player_y == town_y):
                running = False #Stops map loop
                town_menu = True #Sets output of landed on town to True
            #When player on Monster space
            elif (player1.player_x == monster_x) and (player1.player_y == monster_y):
                running = False #Stops map loop
                monster_menu = True #Sets output of landed on monster to True
        
        #fills screen white
        screen.fill((255,255,255))
        #draws maplines
        map1.drawlines(screen)
        #draws town
        map1.drawtown(town_x, town_y, screen)
        #draws monster
        map1.drawmonster(monster_x, monster_y, screen)
        #draws player
        player1.draw_player(screen)
        
        #Keyboard input and control system
        for event in pygame.event.get():
            #if pygame is closed abruptly ends map loop
            if event.type == pygame.QUIT:
                running = False
            #Detects when a key has been pushed down
            elif event.type == pygame.KEYDOWN:
                first_move_done = True
                
                #Moves player up if up arrow is pressed
                if event.key == pygame.K_UP:
                    if player1.player_y >= 32:
                        player1.player_y -= 32
                
                #Moves player down if down arrow is pressed
                elif event.key == pygame.K_DOWN:
                    if player1.player_y < 288:
                        player1.player_y += 32
                
                #moves player left if left arrow is pressed
                elif event.key == pygame.K_LEFT:
                    if player1.player_x >= 32:
                        player1.player_x -= 32
                
                #Moves player right if right arrow is pressed    
                elif event.key == pygame.K_RIGHT:
                    if player1.player_x < 288:
                        player1.player_x += 32
                
                #Exits map abruptly    
                elif event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update() #clears screen
        time.sleep(.01) #Time delay 
    #ends pygame instance
    pygame.quit()
    return player1.player_x, player1.player_y, town_menu, monster_menu
#Map test setup
if __name__ == "__main__":
    print(make_map(32, 32, 32, 32))
