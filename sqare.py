import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(1000,1000)
side=2
angle=360/side
square=turtle.Turtle()
for i in range(side):
    square.forward(50)
    square.right(angle)
turtle.done()