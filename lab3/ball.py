import pygame
from random import randint

class Ball:

    RADIUS = 10

    def __init__(self, screen, border, color, bgcolor, vx = 0, vy = 0, x = 0, y = 0):
        self.screen = screen
        self.border = border
        self.color = color
        self.bgcolor = bgcolor

        self.vx = vx
        self.vy = vy
        
        self.x = x
        self.y = y
        

    def show(self, color=None):
        color = self.color if color is None else color
        pygame.draw.circle( self.screen, color, (self.x, self.y), self.RADIUS )

    def update(self):
        self.show(self.bgcolor)

        if self.x == self.RADIUS + self.border :
            self.vx = -self.vx
            self.color = pygame.Color(randint(0,255),randint(0,255),randint(0,255))
        if self.y == self.RADIUS + self.border or self.y == self.screen.get_rect().height - self.border - self.RADIUS: 
            self.vy = -self.vy
            self.color = pygame.Color(randint(0,255),randint(0,255),randint(0,255))

        self.x += self.vx
        self.y += self.vy
        self.show()
