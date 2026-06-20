import turtle

# Create the turtle
t = turtle.Turtle()
t.speed(3)

# Draw the boat's hull (rectangle)
t.color("brown")
for _ in range(2):
    t.fd(200)  # Forward 200 units (length of the boat)
    t.left(90)
    t.fd(50)   # Forward 50 units (width of the boat)
    t.left(90)
t.color("black")
t.left(90)  # Make sure turtle is facing upwards
t.fd(100)   # Draw the mast
t.color("white") # Draw the sail (triangle)
t.left(45)
t.fd(70)    # First side of the sail
t.left(90)
t.fd(70)    # Second side of the sail
t.left(135)
t.fd(70)    # Third side of the sail
t.hideturtle()
turtle.done()
