import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Pong 0")

    # create a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # rgb background
    screen.fill((0, 0, 0))
    # double buffering: stage all changes and update them all at once
    # avoid flickering
    pygame.display.update()

    # draw walls as rectangles, pygame.draw.rect
    # rect(surface, color, rect) => Rect
    # Rect((left, top), (width, height)) => Rect
    wcolor = pygame.Color("white")

    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))

    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    main()
