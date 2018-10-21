import pygame
from Entities.background import Background
from Entities.hero import Hero
from Entities.enemy import Enemy

def main():
    pygame.init()
    background = Background(['sprites/bg1.png', 'sprites/bg2.png', 'sprites/bg3.png', 'sprites/bg4.png'], (800, 900),
                            'FAR')
    background.draw()
    hero = Hero('sprites/hero.png', 0, 0, 100, 80, 100, 20, 5, background)
    hero.draw()
    playing = True
    enemy =
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving = True
                    while moving:
                        pygame.time.delay(50)
                        hero.move(hero.speed, 0)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_LEFT:
                    moving = True
                    while moving:
                        pygame.time.delay(50)
                        hero.move(-hero.speed, 0)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_UP:
                    moving = True
                    while moving:
                        pygame.time.delay(50)
                        hero.move(0, hero.speed)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_DOWN:
                    moving = True
                    while moving:
                        pygame.time.delay(50)
                        hero.move(0, -hero.speed)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break


if __name__ == '__main__':
    main()
