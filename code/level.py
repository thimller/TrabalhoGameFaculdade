#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display

from code.entityFactory import EntityFactory
from code.entity import Entity




class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('tile'))

    def run(self, ):
        pygame.mixer_music.load("./asset/Musicas/Level.musica.mp3")
        # faz a musica tocar
        pygame.mixer_music.play(-1)
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
        pass