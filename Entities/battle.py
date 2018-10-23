import pygame
from Entities.enemy import Enemy
from Entities.hero import Hero
from text_object import TextObject
from numbers_generators import Lucky_Numbers_Generator, PrimeNumbersGenerator, UlamNumbersGenerator

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
        self.window.blit(self.hero.battle_image, (
            resolution[0] // 4 - self.hero.battle_image.get_width() // 2,
            resolution[1] // 2 - self.hero.battle_image.get_height() // 2))

        hint_text = '''
        To beat your opponent,
        you should determine which sequence contains questioned number,
        if 2 sequences contain number - both answers are correct
        '''

        hint = TextObject(850, 600, lambda: hint_text, (255, 255, 255, 1), 'Consolas', 30)
        hint.draw(window, centralized=True)

        hero_name = TextObject(resolution[0] // 4 - self.hero.battle_image.get_width() // 2,
                               resolution[1] // 2 - self.hero.battle_image.get_height() // 2 - 20, lambda: 'Andriy Roman',
                               (211, 23, 23, 1), 'Consolas', 20)
        hero_name.draw(window)

        self.window.blit(self.opponent.image, (3 * resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                               resolution[1] // 2 - self.opponent.image.get_height() // 2))
        enemy_name = TextObject(3 * resolution[0] // 4 - self.opponent.image.get_width() // 2,
                                resolution[1] // 2 - self.opponent.image.get_height() // 2 - 20,
                                lambda: self.opponent.name, (211, 23, 23, 1), 'Consolas', 20)
        enemy_name.draw(window)

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

