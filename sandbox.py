import pygame
import random
from Entities.background import Background
from Entities.hero import Hero
from Entities.enemy import Enemy

enemies_locations = [[(1000, 50), (220, 500), (300,700)], [(600, 85), (1070, 270), (250, 600)], [(470, 180), (625, 600), (1050, 650)], [(1000, 20), (100, 500), (200,700)]]
enemies_sprites = ['sprites/enemy0.png', 'sprites/enemy1.png', 'sprites/enemy2.png', 'sprites/enemy3.png', 'sprites/enemy4.png', 'sprites/enemy5.png']

def main():
    pygame.init()
    window = pygame.display.set_mode((1918, 1074))
    pygame.display.set_caption('FAR')

    level = 0
    enemies = init_enemies(window, level)

    background = Background(['sprites/bg1.png', 'sprites/bg2.png', 'sprites/bg3.png', 'sprites/bg4.png'], (1918, 1074),
                            window)
    background.draw()
    draw_enemies(enemies)

    hero = Hero('sprites/hero.png', 0, 0, 100, 125, 100, 20, 40, background)
    hero.draw()
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving = True
                    while moving:
                        pygame.time.delay(1)
                        hero.move(hero.speed, 0, enemies)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_LEFT:
                    moving = True
                    while moving:
                        pygame.time.delay(1)
                        hero.move(-hero.speed, 0, enemies)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_UP:
                    moving = True
                    while moving:
                        pygame.time.delay(1)
                        hero.move(0, hero.speed, enemies)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break
                elif event.key == pygame.K_DOWN:
                    moving = True
                    while moving:
                        hero.move(0, -hero.speed, enemies)
                        for stop_event in pygame.event.get():
                            if stop_event.type == pygame.KEYUP and stop_event.key == event.key:
                                moving = False
                                break

def init_enemies(window, lvl=0):
    eminem = []
    i = 0
    locations = enemies_locations[lvl]
    while(i<3):
        location = locations[i]
        sprite = random.choice(enemies_sprites)
        enemy = Enemy(sprite, location[0], location[1], 100, 120, 20, 10, 'Enemy', window)
        eminem.append(enemy)
        i += 1

    return eminem

def draw_enemies(en):
    for e in en:
        e.draw()
        

if __name__ == '__main__':
    main()
