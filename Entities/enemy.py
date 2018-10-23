from .creature import Creature
import pygame


class Enemy(Creature):
    def __init__(self, sprite, x, y, width, height, full_health, damage, name, window):
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.max_health = full_health
        self.health = full_health
        self.name = name
        self.damage = damage
        self.coordinates = [x, y]
        self.window = window

    def draw(self):
        '''
        object -> None 
        Creates and puts the enemies on the playground.
        '''
        self.window.blit(self.image, self.coordinates)
