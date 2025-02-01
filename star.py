import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(1000,1000)
star=turtle.Turtle()
star.color("white")
i=0
while i<5:
    star.forward(50)
    star.left(144)
    i+=1
turtle.done()