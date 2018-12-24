import pygame
import pygame.locals as pgloc

import OpenGL.GL as GL
import OpenGL.GLU as GLU
from graphics.cube import DEFAULT_EDGES, DEFAULT_VERTICES

DISPLAY = (800, 600)


def generate_cube():
    # 1. Tell OpenGL that the code "type" is line-drawing
    GL.glBegin(GL.GL_LINES)

    # 2. For each line, draw it using glVertex3fv
    for edge in DEFAULT_EDGES:
        for v in edge:
            vertex = DEFAULT_VERTICES[v]
            GL.glVertex3fv(vertex)
    GL.glEnd()


def get_display_ratio():
    return DISPLAY[0] / DISPLAY[1]


def main():
    pygame.init()
    # tell pygame it will be using openGL
    pygame.display.set_mode(DISPLAY,
                            pgloc.DOUBLEBUF|pgloc.OPENGL)

    # set openGL perspective
    GLU.gluPerspective(
        45,  # degree of field-of-view
        get_display_ratio(),  # aspect ratio
        0.1,  # znear - near clipping plane
        50  # zfar - far clipping plane
    )

    GL.glTranslatef(0, 0, -5)
    # translate the openGL by x, y, z
    # in this case, we move everything backwards
    # so that we are a bit further from the cubee

    game_alive = True
    game_clock = pygame.time.Clock()

    while game_alive:
        # event checks
        input_x = 1
        input_y = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_alive = False
                pygame.quit()
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            input_y += 5
        if key_pressed[pygame.K_DOWN]:
            input_y -= 5
        if key_pressed[pygame.K_LEFT]:
            input_x -= 5
        if key_pressed[pygame.K_RIGHT]:
            input_x += 5
                

        # rotate openGL world by (angle, x, y, z)
        GL.glRotatef(1, input_x, input_y, 1)
        # clear the world?
        GL.glClear(
            GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT
        )
        # regenerate the cube
        generate_cube()
        # pygame displaying
        pygame.display.flip()
        game_clock.tick(60)


if __name__ == "__main__":
    main()