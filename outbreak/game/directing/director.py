from game.shared.point import Point
import pyray

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
        
    def start_game(self, cast):
        """Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        score = cast.get_first_actor("score")
        reds = cast.get_actors("reds")
        blues = cast.get_actors("blues")

        all_actors_lists = []
        all_actors_lists.append(cast.get_actors("reds"))
        all_actors_lists.append(cast.get_actors("blues"))

        all_actors = [ item for elem in all_actors_lists for item in elem]

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for red in reds:
            red.move_next(max_x, max_y)
            red.bottom_ceiling_collision(max_y)
            red.wall_collision(max_x)
            
        for blue in blues:
            blue.move_next(max_x, max_y)
            blue.bottom_ceiling_collision(max_y)
            blue.wall_collision(max_x)

        for i in range(0, len(all_actors)):
            for j in range(i + 1, len(all_actors)):
        
                first_vector = (all_actors[i].get_position().get_x(), all_actors[i].get_position().get_y())
                second_vector = (all_actors[j].get_position().get_x(), all_actors[j].get_position().get_y())

                #Collision detection
                if pyray.check_collision_circles(first_vector, 12.0, second_vector, 12.0):
                    temp_dx = all_actors[j].get_velocity().get_x()
                    temp_dy = all_actors[j].get_velocity().get_y()

                    all_actors[j].set_velocity(Point(0, 0))

                    dx = all_actors[i].get_velocity().get_x()
                    dy = all_actors[i].get_velocity().get_y()

                    all_actors[i].set_velocity(Point(0, 0))

                    all_actors[j].set_velocity(Point(dx, dy))

                    all_actors[i].set_velocity(Point(temp_dx, temp_dy))

                    if all_actors[i].get_text == "0" and all_actors[j].get_text == "*":
                        pyray.image_color_replace(all_actors[j], pyray.BLUE, pyray.ORANGE)

                    

                #[on_true] if [expression] else [on_false]
                self.score -= 1 if self.score else self.score
                score.set_text(f"Score: {self.score}")

        
            #     score.set_text(f"Score: {self.score}")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer() 