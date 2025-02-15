import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)  # Set the drawing speed

# Function to draw a circle
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.fillcolor(color)
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Function to draw an ellipse (for eyes)
def draw_ellipse(color, x, y, width, height):
    pen.penup()
    pen.fillcolor(color)
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.left(45)
    for _ in range(2):
        pen.circle(width, 90)
        pen.circle(height, 90)
    pen.end_fill()
    pen.setheading(0)

# Draw the head
draw_circle("lightblue", 100, 0, -100)

# Draw the eyes
draw_ellipse("white", -40, 30, 30, 50)  # Left eye white part
draw_ellipse("white", 40, 30, 30, 50)   # Right eye white part
draw_circle("black", 15, -30, 70)       # Left eye pupil
draw_circle("black", 15, 50, 70)        # Right eye pupil

# Draw the mouth
pen.penup()
pen.goto(-30, -20)
pen.pendown()
pen.right(90)
pen.circle(30, 180)
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.left(180)
pen.circle(30, 180)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()