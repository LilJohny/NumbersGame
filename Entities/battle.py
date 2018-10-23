import pygame
from Entities.enemy import Enemy
from Entities.hero import Hero
from text_object import TextObject
from numbers_generators import Lucky_Numbers_Generator, PrimeNumbersGenerator, UlamNumbersGenerator
import static

pygame.init()


class Battle:
    def __init__(self, hero: Hero, opponent: Enemy, window: pygame.Surface, battle_image: str, battle_bg):
        self.hero = hero
        self.opponent = opponent
        self.window = window
        self.battle_image = pygame.image.load(battle_image)
        self.resolution = (self.window.get_width(), self.window.get_height())
        self.battle_image = pygame.transform.scale(self.battle_image, self.resolution)
        self.battle_bg = pygame.image.load(battle_bg)
        self.battle_bg = pygame.transform.scale(self.battle_bg, self.resolution)
        self.window.fill((0, 0, 0))
        self.window.blit(self.battle_bg, (0, 0))
        self.window.blit(self.battle_image, (0, 0))
        self.window.blit(self.hero.battle_image, (
            self.resolution[0] // 4 - self.hero.battle_image.get_width() // 2,
            self.resolution[1] // 2 - self.hero.battle_image.get_height() // 2))
        hint = []
        hint_funcs = [static.text_hint_1, static.text_hint_2, static.text_hint_3, static.text_hint_4,
                      static.text_hint_5, static.text_hint_6]
        i = 0
        for func in hint_funcs:
            hint_piece = TextObject(self.battle_image.get_width() // 2 + 10,
                                    3 * self.battle_image.get_height() // 4 + i, func
                                    , (255, 255, 255, 1), 'Consolas', 15)
            hint.append(hint_piece)
            i += 20

        for var in hint:
            var.draw(window, True)
        hero_name = TextObject(
            self.resolution[0] // 4 - self.hero.battle_image.get_width() // 2 + self.hero.width // 2 + 6,
            self.resolution[1] // 2 - self.hero.battle_image.get_height() // 2 - 20,
            lambda: 'You',
            (255, 215, 0, 1), 'Consolas', 25)
        hero_name.draw(window, True)

        self.window.blit(self.opponent.image, (3 * self.resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                               self.resolution[1] // 2 - self.opponent.image.get_height() // 2))
        enemy_name = TextObject(
            3 * self.resolution[0] // 4 - self.opponent.image.get_width() // 2 + self.opponent.image.get_width() // 2,
            self.resolution[1] // 2 - self.opponent.image.get_height() // 2 - 20,
            lambda: self.opponent.name, (255, 215, 0, 1), 'Consolas', 25)
        enemy_name.draw(window, True)

        ulam_generator = UlamNumbersGenerator()
        prime_generator = PrimeNumbersGenerator()
        lucky_generator = Lucky_Numbers_Generator()

        pygame.display.update()

    def draw_hint(self):
        pass

    def display_next_question(self, number):
        text = 'Which sequence contains' + str(number)
        question = TextObject(200, 600, lambda: text, (255, 255, 255, 1), 'Consolas', 30)

    def execute(self):
        while self.hero.current_health > 0 and self.opponent.health > 0:
            self.display_next_question(5)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.make_damage()

                    elif event.key == pygame.K_2:
                        self.get_damage()

                    elif event.key == pygame.K_3:
                        self.get_damage()

        if self.opponent.health <= 0:
            self.win_battle()

        else:
            self.lose_battle()

    def make_damage(self):
        self.opponent.health -= self.hero.max_damage

    def get_damage(self):
        self.hero.current_health -= self.opponent.damage

    def lose_battle(self):
        print('Battle lost')

    def win_battle(self):
        self.hero.winner = True
        index = self.hero.background.enemies.index(self.opponent)
        del (self.hero.background.enemies[index])
        self.hero.background.draw()
        pygame.display.update()
