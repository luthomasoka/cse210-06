from game.casting.actor import Actor


class Reds(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()

    def bottom_ceiling_collision(self, max_y):
        """ Reverses the direction of the object
        when it collides with the floor or the 
        ceiling

        parameter: The object
        return: The object's vertical velocity
        """
        dy = self._velocity.get_y()

        if self._position.get_y() == 0 or self._position.get_y() == max_y:
            
            dy *= -1

        return self._velocity.set_y(dy)

    def wall_collision(self, max_x):
        """ Reverses the direction of the object
        when it collides with the right or the 
        left side wall

        parameter: The object
        return: The object's horizontal velocity
        """

        dx = self._velocity.get_x()

        if self._position.get_x() == 0 or self._position.get_x() == (max_x - 10):
            
            dx *= -1

        return self._velocity.set_x(dx)
