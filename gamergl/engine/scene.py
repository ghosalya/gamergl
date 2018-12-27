import pygame
from .game_input import GameInput

class Scene:
    """
    Handles units, bodies and game logic.
    """
    def __init__(self):
        self.unit_set = {}
        self.alive = False

    def _get_game_input(self):
        return GameInput()

    def add_unit(self, unit_id, unit):
        self.unit_set[unit_id] = unit

    def handle_default_events(self, game_input):
        for event in game_input.events:
            if event.type == pygame.QUIT:
                self.alive = False


    def setup(self):
        for unit in self.unit_set.values():
            unit.setup()
        self.alive = True

    def frametick(self):
        game_input = self._get_game_input()
        for unit in self.unit_set.values():
            unit.frametick(game_input=game_input)
        
        self.handle_default_events(game_input)
