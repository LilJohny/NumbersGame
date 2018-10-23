import sys

import pygame

from Entities.Objects.text_object import TextObject
from Entities.background import Background
from Entities.hero import Hero
from static import RIGHT, bg_images_paths, scale_screen_resolution, hero_sprites_paths


def main():
    pygame.init()
    window = pygame.display.set_mode((1536, 864), pygame.FULLSCREEN)
    pygame.display.set_caption('FAR')

    background = Background(bg_images_paths, scale_screen_resolution,
                            window)

    background.draw()

    hero = Hero(hero_sprites_paths, 0, 0, 100, 125, 2000,
                1000,
                40, background)
    hero.draw(RIGHT)
    clock = pygame.time.Clock()
    playing = True
    while playing:
        clock.tick(60)
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

                if len(background.enemies) == 0:
                    background.current_level += 1
                    if background.current_level == 4:
                        pygame.display.flip()
                        window.fill((0, 0, 0))
                        win_obj = TextObject(780, 444, lambda: 'YOU ARE PROMOTED', (0, 255, 0, 1), 'Consolas', 70)
                        win_obj.draw(window, centralized=True)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        pygame.display.quit()
                        pygame.quit()
                        sys.exit()
                    else:
                        hero.coordinates = [0, 0]
                        background.set_enemies_strength()
                        background.draw(background.current_level)
                        hero.move(1, 0)
                        pygame.display.update()


if __name__ == '__main__':
    main()
