import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display variables
WIDTH, HEIGHT = 1280, 960
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up asset files
#BALL_IMAGE = pygame.image.load('ball2s.png')

# Set up game variables
ball_x, ball_y = 0, 0
BALL_SPEED = 3
speed_x = random.randint(1,2)
speed_y = random.randint(1,2)

paddle_h=100
paddle_w=20
paddle1_y=HEIGHT/2-paddle_h/2
paddle2_y=HEIGHT/2-paddle_h/2

color=(90,100,12)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     ball_x -= BALL_SPEED
    #     ball_x=max(ball_x,0)
    # if keys[pygame.K_RIGHT]:
    #     ball_x += BALL_SPEED
    #     ball_x=min(ball_x,WIDTH-50)
    # if keys[pygame.K_UP]:
    #     ball_y -= BALL_SPEED
    #     ball_y=max(0, ball_y)
    # if keys[pygame.K_DOWN]:
    #     ball_y += BALL_SPEED
    #     ball_y=min(ball_y, HEIGHT-50)

    # ball movement
    nx=ball_x+speed_x
    ny=ball_y+speed_y

    if nx<10 :
        nx=10
        speed_x = speed_x*-1
    elif nx>WIDTH-10-paddle_w:
        nx=WIDTH-10-paddle_w
        speed_x = speed_x*-1
    
    if ny< 10:
        ny=10
        speed_y = speed_y*-1
    elif ny>HEIGHT:
        ny=HEIGHT
        speed_y = speed_y*-1
    ball_x, ball_y=nx, ny
    
    #padle movement
    if keys[pygame.K_UP]:
        paddle1_y -= BALL_SPEED
        paddle1_y=max(0, paddle1_y)
    if keys[pygame.K_DOWN]:
        paddle1_y += BALL_SPEED
        paddle1_y=min(paddle1_y, HEIGHT-paddle_h)

    if  speed_x > 0 and ball_x > HEIGHT // 2:
        paddle2_y=min(HEIGHT-paddle_h-5, ball_y-random.randint(1,paddle_h // 2))
        

    # Drawing


    win.fill((0, 0, 0))
    #win.blit(BALL_IMAGE, (ball_x, ball_y))
    pygame.draw.circle(win, color, (ball_x, ball_y), 20)

    pygame.draw.rect(win, color, pygame.Rect(10, paddle1_y, paddle_w, paddle_h))
    pygame.draw.rect(win, color, pygame.Rect(WIDTH-paddle_w-10, paddle2_y, paddle_w, paddle_h))

    # Updates the screen
    pygame.display.flip()

pygame.quit()