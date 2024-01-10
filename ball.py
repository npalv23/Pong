import pygame

class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=(90,100,12)

    def draw(self, win):

        pygame.draw.circle(win, self.color, (self.x, self.y), 20)

