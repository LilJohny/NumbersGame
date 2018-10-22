import pygame

pygame.init()


class MovingSystem:
    def __init__(self, hero):
        self.hero = hero

    def work(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    is_moving = True
                    self.hero.move(self.hero.speed, 0)
                    while is_moving:
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                is_moving = False
                                break
                            else:
                                self.hero.move(self.hero.speed, 0)
                elif event.key == pygame.K_LEFT:
                    is_moving = True
                    self.hero.move(-self.hero.speed, 0)
                    while is_moving:
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                is_moving = False
                                break
                            else:
                                self.hero.move(-self.hero.speed, 0)
                if event.key == pygame.K_DOWN:
                    is_moving = True
                    self.hero.move(0, self.hero.speed)
                    while is_moving:
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                is_moving = False
                                break
                            else:
                                self.hero.move(0, self.hero.speed)
                if event.key == pygame.K_UP:
                    is_moving = True
                    self.hero.move(0, -self.hero.speed)
                    while is_moving:
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                is_moving = False
                                break
                            else:
                                self.hero.move(0, -self.hero.speed)
