import pygame
from Entities.enemy import Enemy
from Entities.hero import Hero
from text_object import TextObject

pygame.init()


class Battle:
    def __init__(self, hero: Hero, opponent: Enemy, window: pygame.Surface, battle_image: str):
        self.hero = hero
        self.opponent = opponent
        self.window = window
        self.battle_image = pygame.image.load(battle_image)
        resolution = (self.window.get_width(), self.window.get_height())
        self.battle_image = pygame.transform.scale(self.battle_image, resolution)
        self.window.fill((0, 0, 0))
        self.window.blit(self.battle_image, (0, 0))
        self.window.blit(self.hero.image, (
            resolution[0] // 4 - self.hero.image.get_width() // 2,
            resolution[1] // 2 - self.hero.image.get_height() // 2))
        hero_name = TextObject(self.hero.coordinates[0], self.hero.coordinates[1] - 15, lambda: 'Andriy Roman',
                               (211, 23, 23, 1), 'Consolas', 12)
        hero_name.draw(window)
        pygame.display.update()
        #self.window.blit(self.opponent.image, (3 * resolution[0] // 4 - self.opponent.image.get_width() // 2,
          #                                     resolution[1] // 2 - self.opponent.image.get_height() // 2))
        #pygame.display.update()
        pygame.time.delay(1000000)
