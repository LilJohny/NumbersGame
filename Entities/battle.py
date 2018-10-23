import pygame
import random
import sys
from Entities.enemy import Enemy
from Entities.hero import Hero
from Entities.Objects.text_object import TextObject
from Entities.Objects.bar_object import BarObject
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
        self.hint_funcs = [static.text_hint_1, static.text_hint_2, static.text_hint_3, static.text_hint_4,
                           static.text_hint_5, static.text_hint_6]
        ulam_generator = UlamNumbersGenerator()
        prime_generator = PrimeNumbersGenerator()
        lucky_generator = Lucky_Numbers_Generator()

        self.generators = [ulam_generator, prime_generator, lucky_generator]

        generator = random.choice(self.generators)

        self.number = generator.get_random_number(20)
        self.display_next_question(self.number)
        self.previous_answer = generator.get_generator_name()

        pygame.display.update()

    def draw_hint(self):
        pass

    def display_next_question(self, number):
        self.draw_screen()
        text = 'Which sequence contains ' + str(number) + '?'
        question = TextObject(835, 100, lambda: text, (255, 255, 255, 1), 'Consolas', 30)
        question.draw(self.window, centralized=True)

    def execute(self):
        while self.hero.current_health > 0 and self.opponent.health > 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    pygame.display.update()

                    if event.key == pygame.K_1:
                        self.check_answer(self.number, self.generators[0])

                    elif event.key == pygame.K_2:
                        self.check_answer(self.number, self.generators[1])

                    elif event.key == pygame.K_3:
                        self.check_answer(self.number, self.generators[2])

        if self.opponent.health <= 0:
            self.win_battle()

        else:
            self.lose_battle()

    def check_answer(self, number, generator, length=20):
        if generator.is_from_sequence(number):
            self.make_damage()
        else:
            self.get_damage()
        self.number = self.generate_number()
        self.display_next_question(self.number)
        self.previous_answer = self.answer
        pygame.display.update()

    def generate_number(self, length=20):
        generator = random.choice(self.generators)
        self.answer = generator.get_generator_name()
        return generator.get_random_number(length)

    def make_damage(self):
        self.opponent.health -= self.hero.max_damage
        alert = TextObject(825, 464, lambda: 'RIGHT ANSWER!', (0, 255, 0, 1), 'Consolas', 30)
        alert.draw(self.window, centralized=True)
        pygame.display.update()
        pygame.time.delay(500)

    def get_damage(self):
        self.hero.current_health -= self.opponent.damage
        alert1 = TextObject(825, 454, lambda: 'WRONG ANSWER!', (0, 0, 255, 1), 'Consolas', 30)
        alert2 = TextObject(825, 474, lambda: self.previous_answer, (0, 0, 255, 1), 'Consolas', 30)
        alert1.draw(self.window, centralized=True)
        alert2.draw(self.window, centralized=True)
        pygame.display.update()
        pygame.time.delay(500)

    def lose_battle(self):
        print('Battle lost')
        pygame.display.flip()
        self.window.fill((0, 0, 0))
        lose_obj = TextObject(825, 464, lambda: 'YOU ARE FIRED', (255, 0, 0, 1), 'Consolas', 70)
        lose_obj.draw(self.window, centralized=True)
        pygame.display.update()
        pygame.time.delay(5000)
        sys.exit()

    def win_battle(self):
        self.hero.winner = True
        index = self.hero.background.enemies.index(self.opponent)
        del (self.hero.background.enemies[index])
        self.hero.background.draw()
        del self
        pygame.display.update()

    def draw_screen(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.battle_bg, (0, 0))
        self.window.blit(self.battle_image, (0, 0))
        self.window.blit(self.hero.battle_image, (
            self.resolution[0] // 4 - self.hero.battle_image.get_width() // 2,
            self.resolution[1] // 2 - self.hero.battle_image.get_height() // 2))
        hint = []

        i = 0
        for func in self.hint_funcs:
            hint_piece = TextObject(self.battle_image.get_width() // 2 + 10,
                                    3 * self.battle_image.get_height() // 4 + i, func
                                    , (255, 255, 255, 1), 'Consolas', 15)
            hint.append(hint_piece)
            i += 20

        for var in hint:
            var.draw(self.window, True)
        hero_name = TextObject(
            self.resolution[0] // 4 - self.hero.battle_image.get_width() // 2 + self.hero.width // 2 + 6,
            self.resolution[1] // 2 - self.hero.battle_image.get_height() // 2 - 20,
            lambda: 'You',
            (255, 215, 0, 1), 'Consolas', 25)
        hero_name.draw(self.window, True)
        hero_health_label = TextObject(10, 10, lambda: 'Your health: ', (255, 255, 255, 1), 'Consolas', 20)
        hero_health_bar = BarObject(20, 20, self.hero.max_health, self.hero.current_health, (147, 21, 10, 1),
                                    (14, 108, 23, 1), hero_health_label)
        hero_health_bar.draw(self.window)
        self.window.blit(self.opponent.image, (3 * self.resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                               self.resolution[1] // 2 - self.opponent.image.get_height() // 2 - 20))
        enemy_health_label = TextObject(self.window.get_width() - 200, 10, lambda: self.opponent.name + '`s health: ',
                                        (255, 255, 255, 1), 'Consolas', 20)
        enemy_health_bar = BarObject(self.window.get_width() - 220, 20, self.opponent.max_health, self.opponent.health,
                                     (147, 21, 10, 1),
                                     (14, 108, 23, 1), enemy_health_label)
        enemy_health_bar.draw(self.window)
        enemy_name = TextObject(
            3 * self.resolution[0] // 4 - self.opponent.image.get_width() // 2 + self.opponent.image.get_width() // 2,
            self.resolution[1] // 2 - self.opponent.image.get_height() // 2 - 40,
            lambda: self.opponent.name, (255, 215, 0, 1), 'Consolas', 25)
        enemy_name.draw(self.window, True)
        control_func = [static.control_hint_1, static.control_hint_2, static.control_hint_3, static.control_hint_4]
        control_hints = []
        bias = 0
        for func in control_func:
            control_hint = TextObject(10, 3 * self.window.get_height() // 4 + bias, func, (255, 215, 0, 1),
                                      'Consolas', 20)
            control_hints.append(control_hint)
            bias += 30
        for control_hint in control_hints:
            control_hint.draw(self.window)
