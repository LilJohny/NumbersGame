import pygame


class TextObject:
    def __init__(self, x, y, text_function, color, font_name, font_size):
        self.coordinates = (x, y)
        self.text_func = text_function
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.rect = self.get_surface(text_function())

    def draw(self, surface, centralized=False):
        text_surface, self.rect = self.get_surface(self.text_func())
        if centralized:
            pos = (self.coordinates[0] - self.rect.width // 2, self.coordinates[1])
        else:
            pos = self.coordinates
        surface.blit(text_surface, pos)

    def get_surface(self, text):
        text_surface = self.font.render(text, False, self.color)
        return text_surface, text_surface.get_rect()


