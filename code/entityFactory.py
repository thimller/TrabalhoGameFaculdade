#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'tile':
                list_tile = []
                for i in range(180):
                    #fundo piso
                    list_tile.append(Background('tile102', (735, 405)))
                    list_tile.append(Background('tile101', (687, 405)))
                    list_tile.append(Background('tile104', (639, 405)))
                    list_tile.append(Background('tile102', (591, 405)))
                    list_tile.append(Background('tile106', (543, 405)))
                    list_tile.append(Background('tile101', (495, 405)))
                    list_tile.append(Background('tile102', (447, 405)))
                    list_tile.append(Background('tile101', (399, 405)))
                    list_tile.append(Background('tile104', (351, 405)))
                    list_tile.append(Background('tile102', (303, 405)))
                    list_tile.append(Background('tile106', (255, 405)))
                    list_tile.append(Background('tile101', (207, 405)))
                    list_tile.append(Background('tile101', (159, 405)))
                    list_tile.append(Background('tile104', (111, 405)))
                    list_tile.append(Background('tile102', (63, 405)))
                    list_tile.append(Background('tile106', (15, 405)))
                    list_tile.append(Background('tile101', (0, 405)))

                    #fundo
                    list_tile.append(Background('tile168', (15, 360)))
                    list_tile.append(Background('tile168', (63, 360)))
                    list_tile.append(Background('tile168', (111, 360)))
                    list_tile.append(Background('tile168', (159, 360)))
                    list_tile.append(Background('tile168', (207, 360)))
                    list_tile.append(Background('tile168', (255, 360)))
                    list_tile.append(Background('tile168', (303, 360)))
                    list_tile.append(Background('tile168', (351, 360)))
                    list_tile.append(Background('tile168', (399, 360)))
                    list_tile.append(Background('tile168', (447, 360)))
                    list_tile.append(Background('tile168', (495, 360)))
                    list_tile.append(Background('tile168', (543, 360)))
                    list_tile.append(Background('tile168', (591, 360)))
                    list_tile.append(Background('tile168', (639, 360)))
                    list_tile.append(Background('tile168', (687, 360)))

                    list_tile.append(Background('tile13', (15, 312)))
                    list_tile.append(Background('tile13', (63, 312)))
                    list_tile.append(Background('tile13', (111, 312)))
                    list_tile.append(Background('tile13', (159, 312)))
                    list_tile.append(Background('tile13', (207, 312)))
                    list_tile.append(Background('tile13', (255, 312)))
                    list_tile.append(Background('tile13', (303, 312)))
                    list_tile.append(Background('tile13', (351, 312)))
                    list_tile.append(Background('tile13', (399, 312)))
                    list_tile.append(Background('tile13', (447, 312)))
                    list_tile.append(Background('tile13', (495, 312)))
                    list_tile.append(Background('tile13', (543, 312)))
                    list_tile.append(Background('tile13', (591, 312)))
                    list_tile.append(Background('tile13', (639, 312)))
                    list_tile.append(Background('tile13', (687, 312)))

                    list_tile.append(Background('tile13', (15, 264)))
                    list_tile.append(Background('tile13', (63, 264)))
                    list_tile.append(Background('tile13', (111, 264)))
                    list_tile.append(Background('tile13', (159, 264)))
                    list_tile.append(Background('tile13', (207, 264)))
                    list_tile.append(Background('tile13', (255, 264)))
                    list_tile.append(Background('tile13', (303, 264)))
                    list_tile.append(Background('tile13', (351, 264)))
                    list_tile.append(Background('tile13', (399, 264)))
                    list_tile.append(Background('tile13', (447, 264)))
                    list_tile.append(Background('tile13', (495, 264)))
                    list_tile.append(Background('tile13', (543, 264)))
                    list_tile.append(Background('tile13', (591, 264)))
                    list_tile.append(Background('tile13', (639, 264)))
                    list_tile.append(Background('tile13', (687, 264)))

                    list_tile.append(Background('tile13', (15, 216)))
                    list_tile.append(Background('tile13', (63, 216)))
                    list_tile.append(Background('tile13', (111, 216)))
                    list_tile.append(Background('tile13', (159, 216)))
                    list_tile.append(Background('tile13', (207, 216)))
                    list_tile.append(Background('tile13', (255, 216)))
                    list_tile.append(Background('tile13', (303, 216)))
                    list_tile.append(Background('tile13', (351, 216)))
                    list_tile.append(Background('tile13', (399, 216)))
                    list_tile.append(Background('tile13', (447, 216)))
                    list_tile.append(Background('tile13', (495, 216)))
                    list_tile.append(Background('tile13', (543, 216)))
                    list_tile.append(Background('tile13', (591, 216)))
                    list_tile.append(Background('tile13', (639, 216)))
                    list_tile.append(Background('tile13', (687, 216)))

                    list_tile.append(Background('tile13', (15, 168)))
                    list_tile.append(Background('tile13', (63, 168)))
                    list_tile.append(Background('tile13', (111, 168)))
                    list_tile.append(Background('tile13', (159, 168)))
                    list_tile.append(Background('tile13', (207, 168)))
                    list_tile.append(Background('tile13', (255, 168)))
                    list_tile.append(Background('tile13', (303, 168)))
                    list_tile.append(Background('tile13', (351, 168)))
                    list_tile.append(Background('tile13', (399, 168)))
                    list_tile.append(Background('tile13', (447, 168)))
                    list_tile.append(Background('tile13', (495, 168)))
                    list_tile.append(Background('tile13', (543, 168)))
                    list_tile.append(Background('tile13', (591, 168)))
                    list_tile.append(Background('tile13', (639, 168)))
                    list_tile.append(Background('tile13', (687, 168)))

                    list_tile.append(Background('tile13', (15, 120)))
                    list_tile.append(Background('tile13', (63, 120)))
                    list_tile.append(Background('tile13', (111, 120)))
                    list_tile.append(Background('tile13', (159, 120)))
                    list_tile.append(Background('tile13', (207, 120)))
                    list_tile.append(Background('tile13', (255, 120)))
                    list_tile.append(Background('tile13', (303, 120)))
                    list_tile.append(Background('tile13', (351, 120)))
                    list_tile.append(Background('tile13', (399, 120)))
                    list_tile.append(Background('tile13', (447, 120)))
                    list_tile.append(Background('tile13', (495, 120)))
                    list_tile.append(Background('tile13', (543, 120)))
                    list_tile.append(Background('tile13', (591, 120)))
                    list_tile.append(Background('tile13', (639, 120)))
                    list_tile.append(Background('tile13', (687, 120)))

                    list_tile.append(Background('tile13', (15, 72)))
                    list_tile.append(Background('tile13', (63, 72)))
                    list_tile.append(Background('tile13', (111, 72)))
                    list_tile.append(Background('tile13', (159, 72)))
                    list_tile.append(Background('tile13', (207, 72)))
                    list_tile.append(Background('tile13', (255, 72)))
                    list_tile.append(Background('tile13', (303, 72)))
                    list_tile.append(Background('tile13', (351, 72)))
                    list_tile.append(Background('tile13', (399, 72)))
                    list_tile.append(Background('tile13', (447, 72)))
                    list_tile.append(Background('tile13', (495, 72)))
                    list_tile.append(Background('tile13', (543, 72)))
                    list_tile.append(Background('tile13', (591, 72)))
                    list_tile.append(Background('tile13', (639, 72)))
                    list_tile.append(Background('tile13', (687, 72)))

                    list_tile.append(Background('tile13', (15, 24)))
                    list_tile.append(Background('tile13', (63, 24)))
                    list_tile.append(Background('tile13', (111, 24)))
                    list_tile.append(Background('tile13', (159, 24)))
                    list_tile.append(Background('tile13', (207, 24)))
                    list_tile.append(Background('tile13', (255, 24)))
                    list_tile.append(Background('tile13', (303, 24)))
                    list_tile.append(Background('tile13', (351, 24)))
                    list_tile.append(Background('tile13', (399, 24)))
                    list_tile.append(Background('tile13', (447, 24)))
                    list_tile.append(Background('tile13', (495, 24)))
                    list_tile.append(Background('tile13', (543, 24)))
                    list_tile.append(Background('tile13', (591, 24)))
                    list_tile.append(Background('tile13', (639, 24)))
                    list_tile.append(Background('tile13', (687, 24)))

                    list_tile.append(Background('tile73', (15, 0)))
                    list_tile.append(Background('tile73', (63, 0)))
                    list_tile.append(Background('tile73', (111, 0)))
                    list_tile.append(Background('tile73', (159, 0)))
                    list_tile.append(Background('tile73', (207, 0)))
                    list_tile.append(Background('tile73', (255, 0)))
                    list_tile.append(Background('tile73', (303, 0)))
                    list_tile.append(Background('tile73', (351, 0)))
                    list_tile.append(Background('tile73', (399, 0)))
                    list_tile.append(Background('tile73', (447, 0)))
                    list_tile.append(Background('tile73', (495, 0)))
                    list_tile.append(Background('tile73', (543, 0)))
                    list_tile.append(Background('tile73', (591, 0)))
                    list_tile.append(Background('tile73', (639, 0)))
                    list_tile.append(Background('tile13', (687, 0)))
                    list_tile.append(Background('tile51', (687, 0)))

                    #escadas
                    list_tile.append(Background('tile41', (180, 360)))
                    list_tile.append(Background('tile38', (225, 360)))
                    list_tile.append(Background('tile39', (225, 348)))
                    list_tile.append(Background('tile38', (270, 360)))
                    list_tile.append(Background('tile39', (270, 348)))
                    list_tile.append(Background('tile44', (315, 360)))

                    #piso pulando
                    list_tile.append(Background('tile18', (585,270)))
                    list_tile.append(Background('tile19', (540, 270)))
                    list_tile.append(Background('tile20', (495, 270)))
                    list_tile.append(Background('tile18', (270,180)))
                    list_tile.append(Background('tile19', (225, 180)))
                    list_tile.append(Background('tile20', (180, 180)))
                    list_tile.append(Background('tile18', (90,135)))
                    list_tile.append(Background('tile19', (45, 135)))
                    list_tile.append(Background('tile19', (225, 90)))
                    list_tile.append(Background('tile19', (315, 90)))
                    list_tile.append(Background('tile19', (405, 90)))
                    list_tile.append(Background('tile20', (543, 135)))
                    list_tile.append(Background('tile19', (591, 135)))
                    list_tile.append(Background('tile18', (639, 135)))
                    list_tile.append(Background('tile20', (687, 45)))
                    list_tile.append(Background('tile51', (687, 0)))


                    #parede esquerda
                    list_tile.append(Background('tile118', (0,0)))
                    list_tile.append(Background('tile112', (0,45)))
                    list_tile.append(Background('tile124', (0,90)))
                    list_tile.append(Background('tile122', (0,135)))
                    list_tile.append(Background('tile122', (0,180)))
                    list_tile.append(Background('tile124', (0,225)))
                    list_tile.append(Background('tile124', (0,270)))
                    list_tile.append(Background('tile122', (0,315)))
                    list_tile.append(Background('tile82', (0,360)))

                    #piso
                    list_tile.append(Background('tile45', (45,360)))
                    list_tile.append(Background('tile45', (90,360)))
                    list_tile.append(Background('tile45', (135,360)))
                    list_tile.append(Background('tile45', (180,360)))
                    list_tile.append(Background('tile45', (225,360)))
                    list_tile.append(Background('tile45', (270, 360)))
                    list_tile.append(Background('tile45', (315, 360)))
                    list_tile.append(Background('tile45', (360, 360)))
                    list_tile.append(Background('tile45', (405, 360)))
                    list_tile.append(Background('tile45', (450, 360)))
                    list_tile.append(Background('tile45', (495, 360)))
                    list_tile.append(Background('tile45', (540, 360)))
                    list_tile.append(Background('tile45', (585, 360)))
                    list_tile.append(Background('tile45', (630, 360)))
                    list_tile.append(Background('tile45', (675, 360)))
                    list_tile.append(Background('tile45', (720, 360)))

                    #parede direita
                    list_tile.append(Background('tile121', (735,0)))
                    list_tile.append(Background('tile120', (735,45)))
                    list_tile.append(Background('tile120', (735,90)))
                    list_tile.append(Background('tile116', (735,135)))
                    list_tile.append(Background('tile116', (735,180)))
                    list_tile.append(Background('tile116', (735,225)))
                    list_tile.append(Background('tile120', (735,270)))
                    list_tile.append(Background('tile120', (735,315)))
                    list_tile.append(Background('tile83', (735,360)))




                return list_tile
