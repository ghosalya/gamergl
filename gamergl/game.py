import pygame
import pygame.locals as pgloc

import OpenGL.GL as GL
import OpenGL.GLU as GLU

class GameSession:
    def __init__(self):
        # TODO: read config from TOML
        self.display_size = (800, 600)
        self.fps = 60

    def get_display_ratio(self):
        return self.display_size[0] / self.display_size[1]

    def setup_display(self):
        pygame.display.set_mode(self.display_size, 
                                pgloc.DOUBLEBUF|pgloc.OPENGL)
        # set openGL perspective
        # TODO: implement proper camera object
        GLU.gluPerspective(
            45,
            self.get_display_ratio(),
            0.1, 
            50  
        )
        GL.glTranslatef(0, 0, -15)

    def run(self, scene):
        pygame.init()
        self.setup_display()

        game_clock = pygame.time.Clock()
        scene.setup()

        while scene.alive:
            GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
            
            scene.frametick()

            pygame.display.flip()
            game_clock.tick(self.fps)


