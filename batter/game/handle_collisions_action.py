import random
from game import constants
from game.action import Action
from game.point import Point
import sys

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
        coordinate = self.ball.get_velocity()
        x = coordinate.get_x()
        y = coordinate.get_y()
        _velocity = Point(x * -1, y)
        self.ball.set_velocity(_velocity)


    def _handle_ceiling(self):
        coordinate = self.ball.get_velocity()
        x = coordinate.get_x()
        y = coordinate.get_y()
        _velocity = Point(x, y * -1)
        self.ball.set_velocity(_velocity)



    def _handle_paddle(self):
        coordinate = self.ball.get_velocity()
        x = coordinate.get_x()
        y = coordinate.get_y()
        _velocity = Point(x, y * -1)
        self.ball.set_velocity(_velocity)
        print("enter")


    def _handle_brick(self, n):
        brick = self.bricks[n]
        coordinate = self.ball.get_velocity()
        x = coordinate.get_x()
        y = coordinate.get_y()
        _velocity = Point(x, y * -1)
        self.ball.set_velocity(_velocity)
        self.bricks.pop(n)



    def _handle_floor(self):
        # game over
        sys.exit()


    # function for each
    # ball = cast["ball"] = [ball]
    # collision for wall(s)
    # ceiling
    # brick
    # paddle
    # floor (maybe?)


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.paddle = cast["paddle"][0] # there's only one
        self.ball = cast["ball"][0] # there's only one
        self.bricks = cast["brick"]
        position = self.ball.get_position()
        x = position.get_x()
        y = position.get_y()
        if x == constants.MAX_X:
            print("yes")
        if x == 1 or x == constants.MAX_X - 1:
            self._handle_wall()
        for symbol in range(len(self.paddle.get_text())):
            paddle_position = self.paddle.get_position()
            paddle_position = paddle_position.add(Point(symbol, -1))
            if self.ball.get_position().equals(paddle_position):
                self._handle_paddle()
            elif y == constants.MAX_Y - 1:
                self._handle_floor()
        if y == 1:
            self._handle_ceiling()
        for symbol in range(len(self.bricks) - 1):
            brick = self.bricks[symbol]
            if self.ball.get_position().equals(brick.get_position()):
                self._handle_brick(symbol)
        
