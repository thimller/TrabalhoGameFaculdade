#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # carrega a musica
        pygame.mixer_music.load("./asset/Musicas/Menu.musica.mp3")
        # faz a musica tocar
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.QUIT()
               #     quit()