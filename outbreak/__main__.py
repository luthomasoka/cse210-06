import os
import random

from constants import *

from game.casting.actor import Actor
from game.casting.blues import Blues
from game.casting.reds import Reds
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()

    # create score
    score = Actor()
    score.set_text("Score: 0")
    score.set_font_size(FONT_SIZE)
    score.set_position(Point(10, 0))
    cast.add_actor("score", score)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the Blues 
    for _ in range(DEFAULT_BLUES):
        text = '*'        
    
        x = random.randint(1, COLS - 1)
        y = random.randint(1, COLS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        x = random.randint(3, 7)
        y = random.randint(3, 7)
        velocity = Point(x, y)

        blues = Blues()
        blues.set_text(text)
        blues.set_font_size(FONT_SIZE)
        blues.set_velocity(velocity)
        blues.set_position(position)
        cast.add_actor("blues", blues)

     # create the Reds
    for _ in range(DEFAULT_REDS):
        text = 'o'        
        
        x = random.randint(1, COLS - 1)
        y = random.randint(1, COLS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        x = random.randint(3, 7)
        y = random.randint(3, 7)
        velocity = Point(x, y)
        
        reds = Reds()
        reds.set_text(text)
        reds.set_font_size(FONT_SIZE)
        reds.set_velocity(velocity)
        reds.set_position(position)
        cast.add_actor("reds", reds)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()