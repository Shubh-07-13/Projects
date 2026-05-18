import turtle
turtle.Screen().bgcolor("Blue")
a = turtle.Screen()
a.setup(400,300)
turtle.title("My First Turtle Window!")
b = turtle.Turtle()
for i in range(4):
    b.forward(100)
    b.left(90)
    i += 1