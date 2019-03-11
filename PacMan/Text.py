from pygame import *


class Text(object):
    """Rendering Texts and Fonts."""
    def __init__(self, text_font, size, message, colors, x_pos, y_pos):
        self.font = font.Font(text_font, size)
        self.surface = self.font.render(message, True, colors)
        self.rect = self.surface.get_rect(topleft=(x_pos, y_pos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
