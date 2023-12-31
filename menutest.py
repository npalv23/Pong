from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
W_WIDTH=600
W_HEIGHT=400

surface = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

def level_menu():
    mainmenu._open(level)

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    playername=userName.get_value()
    print(playername)
    pass




mainmenu= pygame_menu.Menu("Welcome", W_WIDTH, W_HEIGHT, theme=themes.THEME_SOLARIZED)
userName = mainmenu.add.text_input('Name: ', default='Avatar')
loading = pygame_menu.Menu("Loading the Game", W_WIDTH, W_HEIGHT, theme=themes.THEME_ORANGE)
loading.add.progress_bar('Progress', prgressbar_id='1', default=0, width = 200)


mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Select a Difficulty', 600, 400, 
                                 theme=themes.THEME_BLUE)
level.add.selector('Difficulty:',[('Hard',1),('Easy',2)], onchange=set_difficulty)

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
  
    pygame.display.update()