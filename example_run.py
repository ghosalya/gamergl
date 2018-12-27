from gamergl import GameSession, Unit, UnitAspect, Scene, Body2D, Body2DController
import OpenGL.GL as GL

square_vertices = (
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1)
)

square_edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)

def square_definition(center, rotation, scale):
    # for now ignore rotation
    # lupsup - abrupt change to 3d
    new_vertices = [
        (vertex[0] * scale[0] + center[0],
         vertex[1] * scale[1] + center[1],
         0)
        for vertex in square_vertices
    ]

    GL.glBegin(GL.GL_LINES)
    for edge in square_edges:
        for v in edge:
            vertex = new_vertices[v]
            GL.glVertex3fv(vertex)
    GL.glEnd()


def main():
    game_session = GameSession()
    game_scene = Scene()

    player_unit = Unit(game_scene, "player")
    player_body_aspect = Body2D(player_unit,
                                body_definition=square_definition)
    player_body_controller = Body2DController(player_unit, player_body_aspect)

    player_body_aspect.rotation = 15
    player_body_aspect.scale_all(0.5)
    player_body_controller.speed = 0.2

    other_unit = Unit(game_scene, "other")
    other_unit_body_aspect = Body2D(other_unit,
                                    body_definition=square_definition)
    other_unit_body_aspect.translate(1, 2)
    other_unit_body_aspect.rotate(-12)

    game_session.run(game_scene)


if __name__ == "__main__":
    main()