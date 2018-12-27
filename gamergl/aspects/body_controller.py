import pygame
from ..abstracts.unit import UnitAspect

class Body2DController(UnitAspect):
    def __init__(self, unit, body_aspect):
        super(Body2DController, self).__init__(unit)
        self.body_aspect = body_aspect
        self.speed = 0.05

    def get_translation_from_input(self, game_input):
        input_x = 0
        input_x += self.speed * game_input.key_is_pressed(pygame.K_RIGHT)
        input_x -= self.speed * game_input.key_is_pressed(pygame.K_LEFT)

        input_y = 0
        input_y += self.speed * game_input.key_is_pressed(pygame.K_UP)
        input_y -= self.speed * game_input.key_is_pressed(pygame.K_DOWN)

        input_rotate = 0
        input_rotate += game_input.key_is_pressed(pygame.K_d)
        input_rotate -= game_input.key_is_pressed(pygame.K_a)

        return input_x, input_y, input_rotate

    def setup(self):
        pass

    def frametick(self, game_input=None):
        x, y, rotation = self.get_translation_from_input(game_input)
        self.body_aspect.translate(x, y)
        self.body_aspect.rotate(rotation)
