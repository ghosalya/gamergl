from ..abstracts.unit import UnitAspect

import OpenGL.GL as GL

class Body2D(UnitAspect):
    def __init__(self, unit, body_definition=None):
        '''
        :param body_definition: a function calling for OpenGL to draw the body,
            taking in center (tuple), rotation (angle) and scale (tuple)
        '''
        super(Body2D, self).__init__(unit)
        self.center = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)

        self.definition = body_definition

    # Aspect Functions
    def draw(self):
        GL.glRotatef(-self.rotation, 0, 0, 1)
        self.definition(self.center, self.rotation, self.scale)
        GL.glRotatef(self.rotation, 0, 0, 1)

    def translate(self, x, y, relative_to_world=False):
        if relative_to_world:
            # TODO: implement the translation with rotation
            pass
        else:
            self.center = (
                self.center[0] + x,
                self.center[1] + y
            )

    def rotate(self, angle):
        self.rotation = (self.rotation + angle) % 360

    def scale_all(self, ratio, absolute=False):
        if absolute:
            self.scale = (ratio, ratio)
        else:
            self.scale = (
                self.scale[0] * ratio,
                self.scale[1] * ratio
            )


    # API calls
    def setup(self):
        if self.definition is None:
            raise NotImplementedError()

    def frametick(self, game_input=None):
        self.draw()