#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_RED, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        # add imagem
        self.surf = pygame.image.load("./asset/MenuPNG.png")
        # cria um retangulo
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        # carrega a musica
        pygame.mixer_music.load("./asset/Musicas/Menu.musica.mp3")
        # faz a musica tocar
        pygame.mixer_music.play(-1)

        while True:
            # desenhando a imagem no retangulo
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(50,"Castle",COLOR_RED,((WIN_WIDTH/2), 70))
            self.menu_text(50,"Climb",COLOR_RED,((WIN_WIDTH/2), 120))


            for i in range(len(MENU_OPTION)):
                self.menu_text(30,MENU_OPTION(i),COLOR_RED,((WIN_WIDTH/2), 200 + 25 * i))
                
            # mostrando a imagem na tela
            pygame.display.flip()

            #checa o evento para poder fechar o prog no 'x'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        text_surf: Surface = text_font.render(text,True,text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)
