#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        # add imagem
        self.surf = pygame.image.load("./asset/MenuPNG.png")
        # cria um retangulo
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        #desenhando a imagem no retangulo
        self.window.blit(source=self.surf, dest=self.rect)
        #mostrando a imagem na tela
        pygame.display.flip()
        pass
