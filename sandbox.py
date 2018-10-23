import pygame
from Entities.background import Background
from Entities.hero import Hero


def main():
    pygame.init()
    window = pygame.display.set_mode((1650, 928))
    # window = pygame.display.set_mode((1800, 850), pygame.FULLSCREEN)
    pygame.display.set_caption('FAR')

    background = Background(['sprites/bg1.png', 'sprites/bg2.png', 'sprites/bg3.png', 'sprites/bg4.png'], (1918, 1074),
                            window)
    background.draw()

    hero = Hero(['sprites/idle_left.png', 'sprites/idle_right.png', 'sprites/run_left_1.png', 'sprites/run_left_2.png',
                 'sprites/run_left_3.png', 'sprites/run_left_4.png', 'sprites/run_left_5.png',
                 'sprites/run_right_1.png', 'sprites/run_right_2.png', 'sprites/run_right_3.png',
                 'sprites/run_right_4.png', 'sprites/run_right_5.png', 'sprites/idle_battle.png'], 0, 0, 100, 125, 100,
                20,
                40, background)
    hero.draw('right')
    clock = pygame.time.Clock()
    playing = True
    while playing:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving = True
                    while moving:
                        if hero.coordinates[0] < window.get_width() - hero.width - 10:
                            hero.move(hero.speed, 0)
                        for stop_event in pygame.event.get():
                            if (stop_event.type == pygame.KEYUP and stop_event.key == event.key) or hero.winner:
                                if hero.winner:
                                    hero.move(1, 0)
                                hero.winner = False
                                moving = False
                                break
                elif event.key == pygame.K_LEFT:
                    moving = True
                    while moving:
                        if hero.coordinates[0] >= 10:
                            hero.move(-hero.speed, 0)
                        for stop_event in pygame.event.get():
                            if (stop_event.type == pygame.KEYUP and stop_event.key == event.key) or hero.winner:
                                if hero.winner:
                                    hero.move(-1, 0)
                                hero.winner = False
                                moving = False
                                break
                elif event.key == pygame.K_UP:
                    moving = True
                    while moving:
                        if hero.coordinates[1] >= 5:
                            hero.move(0, -hero.speed)
                        for stop_event in pygame.event.get():
                            if (stop_event.type == pygame.KEYUP and stop_event.key == event.key) or hero.winner:
                                if hero.winner:
                                    hero.move(0, 1)
                                hero.winner = False
                                moving = False
                                break
                elif event.key == pygame.K_DOWN:
                    moving = True
                    while moving:
                        if hero.coordinates[1] < window.get_height() - hero.height:
                            hero.move(0, hero.speed)
                        for stop_event in pygame.event.get():
                            if (stop_event.type == pygame.KEYUP and stop_event.key == event.key) or hero.winner:
                                if hero.winner:
                                    hero.move(0, -1)
                                hero.winner = False
                                moving = False
                                break

                elif event.key == pygame.K_ESCAPE:
                    playing = False
                    break


if __name__ == '__main__':
    main()
