import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def __init_(self, cast):
        ball = cast["ball"][0]
        brick = cast["brick"]
        paddle = cast["paddle"][0]
    

    def _handle_wall(self):
        if ball.get_x() == 0 or ball.get_x() == constants.MAX_X:
            coordinate = ball.get_velocity()
            x = coordinate[0]
            y = coordinate[1]
            _velocity = Point(x * -1, y)
            ball.set_velocity(_velocity)


    def _handle_ceiling(self):
        if ball.get_y() == 0:
            pass



    def _handle_paddle(self):
        pass



    def _handle_brick(self):
        pass



    def _handle_floor(self):
        # game over
        pass


    # function for each
    # ball = cast["ball"] = [ball]
    # collision for wall(s)
    # ceiling
    # brick
    # paddle
    # floor (maybe?)


    # def execute(self, cast):
    #     """Executes the action using the given actors.

    #     Args:
    #         cast (dict): The game actors {key: tag, value: list}.
    #     """
    #     marquee = cast["marquee"][0] # there's only one
    #     robot = cast["robot"][0] # there's only one
    #     artifacts = cast["artifact"]
    #     marquee.set_text("")
    #     for artifact in artifacts:
    #         if robot.get_position().equals(artifact.get_position()):
    #             description = artifact.get_description()
    #             marquee.set_text(description)