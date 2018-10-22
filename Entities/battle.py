import pygame
from Entities.enemy import Enemy
from Entities.hero import Hero
from text_object import TextObject
from numbers_generators import Lucky_Numbers_Generator,PrimeNumbersGenerator,UlamNumbersGenerator
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
        hero_name = TextObject(resolution[0] // 4 - self.hero.image.get_width() // 2,
                               resolution[1] // 2 - self.hero.image.get_height() // 2 - 20, lambda: 'Andriy Roman',
                               (211, 23, 23, 1), 'Consolas', 20)
        hero_name.draw(window, centralized=False)

        self.window.blit(self.opponent.image, (3 * resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                               resolution[1] // 2 - self.opponent.image.get_height() // 2))
        enemy_name = TextObject(3 * resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                resolution[1] // 2 - self.opponent.image.get_height() // 2 - 20,
                                lambda: self.opponent.name, (211, 23, 23, 1), 'Consolas', 20)
        enemy_name.draw(window, centralized=False)
        pygame.display.update()
        ulam_generator =
    def display_next_question(self):

    def execute(self):
        while self.hero.current_health>0 and self.opponent.health>0:

