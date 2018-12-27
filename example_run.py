from gamergl import GameSession, Unit, UnitAspect, Scene
from gamergl.aspects import Body2D, Body2DController
from gamergl.graphics.geometry2D import square_definition, triangle_definition

class ConstantRotation(UnitAspect):
    def __init__(self, unit, body_aspect, rotate_rate):
        super(ConstantRotation, self).__init__(unit)
        self.body_aspect = body_aspect
        self.rotate_rate = rotate_rate
    
    def frametick(self, game_input=None):
        self.body_aspect.rotate(self.rotate_rate)


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
                                    body_definition=triangle_definition)
    other_unit_rotate_aspect = ConstantRotation(other_unit,
                                                other_unit_body_aspect,
                                                2)
    other_unit_body_aspect.translate(1, 2)

    game_session.run(game_scene)


if __name__ == "__main__":
    main()