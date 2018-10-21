from .creature import Creature
import pygame


class Enemy(Creature):
    def __init__(self, sprite, x, y, width, height, full_health, damage, name, background):
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.background = background
        self.max_health = full_health
        self.health = full_health
        self.name = name
        self.damage = damage
        self.coordinates = [x, y]

    def draw(self):
        self.background.window.blit(self.image, self.coordinates)
        pygame.display.update()

