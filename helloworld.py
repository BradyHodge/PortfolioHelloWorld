# Imports
import turtle

# Set vars for the screen
screen = turtle.Screen()
screen.title("Hello World with Turtle")

# Create a object
jeff = turtle.Turtle()

# Set the turtle's attributes
jeff.color("purple")
jeff.pensize(3)

# Move the turtle to the starting position
jeff.penup()
jeff.goto(-100, 0)
jeff.pendown()

# Write Hello World
jeff.write("Hello, World!", font=("Arial", 24, "normal"))

# Hide the turtle
jeff.hideturtle()

# Keep the window open
turtle.done()

