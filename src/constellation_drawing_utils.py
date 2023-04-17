# This program draws the stars of the Orion constellation
# the names of the stars, and the constellation lines.

import turtle
from src.constants import (
    Betelgeuse, 
    Meissa, 
    Alnitak, 
    Alnilam, 
    Mintaka, 
    Saiph, 
    Rigel
)

def draw_orion_constellation():
    # Set the window size.
    turtle.setup(500, 600)

    # Set the window size.
    turtle.penup()
    turtle.hideturtle()

    # Create name constants for the star coordinates.
    LEFT_SHOULDER_X = -70
    LEFT_SHOULDER_Y = 200

    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 180

    LEFT_BELTSTAR_X = -40
    LEFT_BELTSTAR_Y = -20

    MIDDLE_BELTSTAR_X = 0
    MIDDLE_BELTSTAR_Y = 0

    RIGHT_BELTSTAR_X = 40
    RIGHT_BELTSTAR_Y = 20

    LEFT_KNEE_X = -90
    LEFT_KNEE_Y = -180

    RIGHT_KNEE_X = 120
    RIGHT_KNEE_Y = -140

    # Draw the stars.
    turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
    turtle.dot()
    turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    turtle.dot()
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.dot()
    turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    turtle.dot()
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.dot()
    turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
    turtle.dot()
    turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
    turtle.dot()

    # Display the star names
    turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
    turtle.write(Betelgeuse, font=("Arial", 16, "normal"))
    turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    turtle.write(Meissa, font=("Arial", 16, "normal"))
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.write(Alnitak, font=("Arial", 16, "normal"))
    turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    turtle.write(Alnilam, font=("Arial", 16, "normal"))
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.write(Mintaka, font=("Arial", 16, "normal"))
    turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
    turtle.write(Saiph, font=("Arial", 16, "normal"))
    turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
    turtle.write(Rigel, font=("Arial", 16, "normal"))

    # Draw a line from the left shoulder to left belt star
    turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
    turtle.pendown()
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.penup()

    # Draw a line from the right shoulder to right belt star
    turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    turtle.pendown()
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.penup()

    # Draw a line from the left belt star to middle belt star
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    turtle.penup()

    # Draw a line from the middle belt star to right belt star
    turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.penup()

    # Draw a line from the left belt star to left knee
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
    turtle.penup()

    # Draw a line from the right belt star to right knee
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
    turtle.penup()

    # Keep the window open. (Not necessary with IDLE.)
    turtle.done()