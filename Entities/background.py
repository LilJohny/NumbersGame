import pygame

pygame.init()


class Background:
    def __init__(self, image_names, resolution, caption):
        self.levels = []
        self.window = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
        self.current_level = 0
        for image_name in image_names:
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, resolution)
            self.levels.append(image)

    def draw(self, level_number=0):
        self.window.blit(self.levels[level_number], (0, 0))
        pygame.display.update()
        self.current_level = level_number
