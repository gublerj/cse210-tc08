import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #ball = cast["ball"][0] # there's only one
        #paddle = cast["paddle"][0] # there's only one
        #bricks = cast["brick"]
        #marquee.set_text("")
        #for artifact in artifacts:
            #if ball.get_position().equals(paddle.get_position()):
                #self.handle_paddle_collision()
            #elif #wall collision 
            #elif #brick collision
            #elif #ceiling collision
            #elif: #floor collision
        pass
                