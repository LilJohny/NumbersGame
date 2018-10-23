from .creature import Creature
import pygame

pygame.init()


class Hero(Creature):
    def __init__(self, image_names, x, y, width, height, full_health, damage, speed, background):
        self.coordinates = [x, y]
        self.max_health = full_health
        self.current_health = full_health
        self.images_right = []
        self.images_left = []
        self.images_idle = []
        for image_name in image_names:
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, (width, height))
            if image_name.count('battle') == 1:
                self.battle_image = image
            if image_name.count('idle') == 1:
                self.images_idle.append(image)
            elif image_name.count('right') == 1:
                self.images_right.append(image)
            else:
                self.images_left.append(image)
        self.winner = False
        self.width = width
        self.height = height
        self.animation_count = 0
        self.max_damage = damage
        self.background = background
        self.speed = speed

    def draw(self, direction):
        if direction == 'right':
            self.background.window.blit(self.images_right[self.animation_count // 6], self.coordinates)
            self.animation_count += 1
        if direction == 'left':
            self.background.window.blit(self.images_left[self.animation_count // 6], self.coordinates)
            self.animation_count += 1
        if direction == 'up' or direction == 'down':
            self.background.window.blit(self.images_idle[self.animation_count // 15], self.coordinates)
            self.animation_count += 1
        if self.animation_count >= 30:
            self.animation_count = 0
        pygame.display.update()

    def move(self, x, y):  # x is difference between current position x and new, y the same
        self.coordinates[0] += x
        self.coordinates[1] += y
        if x > 0:
            direction = 'right'
        elif x < 0:
            direction = 'left'
        elif y > 0:
            direction = 'up'
        elif y < 0:
            direction = 'down'
        self.background.draw(self.background.current_level)
        self.draw(direction)
        self.check_if_battle_needed()

    def check_if_battle_needed(self):
        for enemy in self.background.enemies:
            if abs(self.coordinates[0] - enemy.coordinates[0]) < 100 and abs(
                    self.coordinates[1] - enemy.coordinates[1]) < 120:
                self.background.start_battle(self, enemy)
