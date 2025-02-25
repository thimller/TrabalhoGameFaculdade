import pygame

pygame.init()

windoll = pygame.display.set_mode(size=(600,480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            quit()