import pygame


class Food:
    position = (0, 0)
    nutrition = 0
    r = 2

    def __init__(self, _position, _nutrition) -> None:
        self.position = _position
        self.nutrition = _nutrition

    def draw(self, DISPLAY):
        food_color = (0, 255, 0)
        if self.nutrition < 0:
            food_color = (255, 0, 0)

        pygame.draw.circle(DISPLAY, food_color, self.position, self.r)