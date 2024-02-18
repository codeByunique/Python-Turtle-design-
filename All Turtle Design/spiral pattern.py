import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")

# Draw a spiral
for i in range(100):
    pen.forward(i * 5)
    pen.right(144)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
