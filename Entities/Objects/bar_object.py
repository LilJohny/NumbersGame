import pygame
from Entities.Objects.text_object import TextObject

pygame.init()


class BarObject:
    def __init__(self, x, y, max_value, current_value, bg_color, fg_color, label: TextObject):
        self.coordinates = [x, y]
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.max_value = max_value
        self.current_value = current_value
        self.label = label

    def update_value(self, value):
        self.current_value = value

    def draw(self, window):
        self.label.draw(window)
        pygame.draw.rect(window, self.bg_color,
                         [self.coordinates[0], self.coordinates[1] + self.label.rect[3], 200, 30])
        if self.current_value != 0:
            pygame.draw.rect(window, self.fg_color,
                             [self.coordinates[0], self.coordinates[1] + self.label.rect[3],
                              (self.current_value / self.max_value) * 200, 30])
