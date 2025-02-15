import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(5)
pen.width(3)

# Function to draw a heart
def draw_heart():
    pen.begin_fill()
    pen.fillcolor("red")
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Draw the heart
draw_heart()

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()