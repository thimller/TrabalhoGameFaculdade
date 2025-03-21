#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'tile1':
                list_tile = []
                for i in range(180):
                    list_tile.append(Background(f'tile{i}', (0,0)))
                return list_tile
