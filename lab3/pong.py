import pygame
from paddle import Paddle
from ball import Ball

from random import randint

def main():
    pygame.init()
    pygame.display.set_caption("Pong 0")

    # create a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 30

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # rgb background
    screen.fill((0, 0, 0))
    # double buffering: stage all changes and update them all at once
    # avoid flickering
    pygame.display.update()

    # draw walls as rectangles, pygame.draw.rect
    # rect(surface, color, rect) => Rect
    # Rect((left, top), (width, height)) => Rect
    white = pygame.Color("white")
    black = pygame.Color("black")

    # top wall
    pygame.draw.rect(screen, white, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # left wall
    pygame.draw.rect(screen, white, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # bottom wall
    pygame.draw.rect(screen, white, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))

    #Ball init
    offset = BORDER + Ball.RADIUS

    x0 = WIDTH - Ball.RADIUS*2
    y0 =  HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = VELOCITY if randint(0,2) else -VELOCITY


    b0 = Ball(screen, BORDER, white, black, vx = vx0, vy = vy0,x = x0, y = y0)
    b0.show()

    pygame.display.update()

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
        clock.tick(FPS)

        b0.update()


if __name__ == "__main__":
    main()


# TODO
# push pong_lab3.py to git + capture a gif and include in your README.md
# GIF: shows collision with the ball and rand start
