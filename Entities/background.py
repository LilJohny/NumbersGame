import pygame
import random

from Entities.battle import Battle
from Entities.enemy import Enemy

pygame.init()


class Background:

    def __init__(self, image_names, resolution, window):
        self.enemies_sprites = ['sprites/enemy0.png', 'sprites/enemy1.png', 'sprites/enemy2.png', 'sprites/enemy3.png',
                                'sprites/enemy4.png', 'sprites/enemy5.png']
        self.current_level = 0
        self.enemies_locations = [[(1000, 50), (220, 500), (300, 700)], [(600, 85), (1070, 270), (250, 600)],
                                  [(470, 180), (625, 600), (1050, 650)], [(1000, 20), (100, 500), (200, 700)]]
        self.window = window
        enemy1 = Enemy(random.choice(self.enemies_sprites), self.enemies_locations[self.current_level][0][0],
                       self.enemies_locations[self.current_level][0][1], 100, 120, 20, 10, 'Enemy1', self.window)
        enemy2 = Enemy(random.choice(self.enemies_sprites), self.enemies_locations[self.current_level][1][0],
                       self.enemies_locations[self.current_level][1][1], 100, 120, 20, 10, 'Enemy2', self.window)
        enemy3 = Enemy(random.choice(self.enemies_sprites), self.enemies_locations[self.current_level][2][0],
                       self.enemies_locations[self.current_level][2][1], 100, 120, 20, 10, 'Enemy3', self.window)
        self.enemies = [enemy1, enemy2, enemy3]
        self.levels = []

        self.current_level = 0
        for image_name in image_names:
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, resolution)
            self.levels.append(image)

    def draw(self, level_number=0):
        self.window.fill((0, 0, 0))
        self.window.blit(self.levels[level_number], (0, 0))
        for enemy in self.enemies:
            enemy.draw()
        self.current_level = level_number

    def start_battle(self, hero, opponent):
        print("Start Battle")
        battle = Battle(hero, opponent, self.window, 'sprites/battle.png')
        battle.execute()
