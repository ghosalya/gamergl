import pygame

class Unit:
    def __init__(self, scene, unit_id):
        self.id = unit_id
        scene.add_unit(unit_id, self)
        self.setup_done = False
        self.aspects = set()

    def setup(self):
        for aspect in self.aspects:
            aspect.setup()

    def frametick(self, game_input=None):
        for aspect in self.aspects:
            aspect.frametick(game_input=game_input)


class UnitAspect:
    def __init__(self, unit):
        unit.aspects.add(self)
        self.setup_done = False

    def setup(self):
        '''
        A function to set up the unit. Any piece of code belonging to this
        unit and is executed at the start of the game should be put here.
        '''
        pass
        

    def frametick(self, game_input=None):
        '''
        A function that runs for every frame. Any code that is updated
        continuously should go here.
        '''
        pass