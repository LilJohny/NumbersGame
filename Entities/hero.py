from .creature import Creature
import pygame

pygame.init()


class Hero(Creature):
    def __init__(self, image_name, x, y, width, height, full_health, damage, speed, background):
        self.coordinates = [x, y]
        self.max_health = full_health
        self.current_health = full_health
        self.image = pygame.image.load(image_name)
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.max_damage = damage
        self.background = background
        self.speed = speed

    def draw(self):
        self.background.window.blit(self.image, self.coordinates)
        pygame.display.update()

    def move(self, x, y):  # x is difference between current position x and new, y the same
        self.coordinates[0] += x
        self.coordinates[1] -= y
        self.background.draw(self.background.current_level)
        self.draw()
        self.check_if_battle_needed()

    def check_if_battle_needed(self):
        for enemy in self.background.enemies:
            if(abs(self.coordinates[0] - enemy.coordinates[0]) < 100 and abs(self.coordinates[1] - enemy.coordinates[1]) < 120):
                self.background.start_battle(self, enemy)