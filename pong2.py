__all__ = ['main']

import pygame
import pygame_menu
import random
from pygame_menu.examples import create_example_window

from random import randrange
from typing import Tuple, Any, Optional, List

WIDTH, HEIGHT = 1280, 960
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60
DIFFICULTY = [1]

clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None

def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.

    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    #DIFFICULTY[0] = difficulty
    DIFFICULTY[0] = index


def play_function(difficulty: List, font: 'pygame.font.Font', test: bool = False) -> None:

    difficulty = difficulty[0]
    print(difficulty)

    global clock
    global main_menu
    global surface

    main_menu.disable()
    main_menu.full_reset()

    BALL_RADIUS=15
    speed_x = random.randint(1,10) * difficulty
    speed_y = random.randint(1,8) * difficulty

    PADDLE_SPEED = speed_y + random.randint(3,12)

    paddle_h=100
    paddle_w=20
    margin_x=10
    margin_y=10
    paddle1_y=HEIGHT/2-paddle_h/2
    paddle2_y=HEIGHT/2-paddle_h/2

    ball_x, ball_y = random.randint(paddle_w+margin_x+BALL_RADIUS+2, WIDTH-margin_x-paddle_w), random.randint(margin_x+BALL_RADIUS+2, HEIGHT -margin_y-paddle_h)

    color=(90,100,12)


    while True:

        # noinspection PyUnresolvedReferences
        clock.tick(FPS)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 221
                    return

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        # Continue playing
        nx=ball_x+speed_x
        ny=ball_y+speed_y

        if nx<margin_x + paddle_w+BALL_RADIUS :
            if ny<paddle1_y or ny >paddle1_y+paddle_h: 
                if nx < -BALL_RADIUS:
                    main_menu.enable()
                    return
            else:
                nx=margin_x + paddle_w+BALL_RADIUS
                speed_x = speed_x*-1


        elif nx>WIDTH-margin_x-paddle_w-BALL_RADIUS:
            nx=WIDTH-margin_x-paddle_w-BALL_RADIUS
            speed_x = speed_x*-1
        
        if ny< margin_y+BALL_RADIUS:
            ny=margin_y+BALL_RADIUS
            speed_y = speed_y*-1
        elif ny>HEIGHT-BALL_RADIUS:
            ny=HEIGHT-BALL_RADIUS
            speed_y = speed_y*-1
        ball_x, ball_y=nx, ny
        
        keys = pygame.key.get_pressed()
        
        #padle movement
        if keys[pygame.K_UP]:
            paddle1_y -= PADDLE_SPEED
            paddle1_y=max(0, paddle1_y)
        if keys[pygame.K_DOWN]:
            paddle1_y += PADDLE_SPEED
            paddle1_y=min(paddle1_y, HEIGHT-paddle_h)

        if  speed_x > 0 and ball_x > WIDTH - WIDTH // 4:
            paddle2_y=min(HEIGHT-paddle_h-margin_y, ball_y-paddle_h // 2)

        surface.fill((0, 0, 0))
        pygame.draw.circle(surface, color, (ball_x, ball_y), BALL_RADIUS)

        pygame.draw.rect(surface, color, pygame.Rect(margin_x, paddle1_y, paddle_w, paddle_h))
        pygame.draw.rect(surface, color, pygame.Rect(WIDTH-paddle_w-margin_x, paddle2_y, paddle_w, paddle_h))

        pygame.display.flip()


def main_background() -> None:
    """
    Function used by menus, draw on background while menu is active.
    """
    global surface
    surface.fill((0, 0, 0))

def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window('Pong game', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Play Menu',
        width=WINDOW_SIZE[0] * 0.75
    )

    
    play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function, DIFFICULTY,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))

    play_menu.add.selector('Select difficulty ',
                           [('1 - Easy', 'EASY'),
                            ('2 - Medium', 'MEDIUM'),
                            ('3 - Hard', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0] * 0.6
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
