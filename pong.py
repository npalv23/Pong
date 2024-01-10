
import pygame
import pygame_menu
from pygame_menu import themes
from mwindow import MainWindow
from ball import Ball




pygame.init()

winMeta=MainWindow(1280, 960)
win = pygame.display.set_mode((winMeta.width, winMeta.height))

def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.

    """
    global mainmenu
    global ball
    global win

    mainmenu.disable()
    mainmenu.full_reset()
    while True:

        # noinspection PyUnresolvedReferences

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    mainmenu.enable()

                    # Quit this function, then skip to loop of main-menu on line 221
                    return

        # Pass events to main_menu
        if mainmenu.is_enabled():
            mainmenu.update(events)

        # Continue playing
        ball.draw(win)
        pygame.display.flip()
    

    #win.fill((0, 0, 0))

#    playername=userName.get_value()
#    print(playername)

ball=Ball(20,20)

mainmenu= pygame_menu.Menu("Welcome", 600, 400, theme=themes.THEME_SOLARIZED)
userName = mainmenu.add.text_input('Name: ', default='Avatar')

mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
mainmenu.center_content()

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(win)

        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(win, mainmenu.get_current().get_selected_widget())
  


    pygame.display.update()