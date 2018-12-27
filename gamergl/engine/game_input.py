import pygame

class GameInput:
    '''
    A data structure that represents events
    and the keys being pressed. 
    (Right now just a pygame wrapper)
    '''
    def __init__(self):
        self.events = pygame.event.get()
        self._key_pressed = pygame.key.get_pressed()

    @property
    def key_pressed(self):
        return self._key_pressed[:]

    def key_is_pressed(self, key):
        return self._key_pressed[key]