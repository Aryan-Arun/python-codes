import turtle
import random
screen=turtle.Screen()
screen.setup(800,600)
t=turtle.Turtle()

x=(input("choose a shape out of these three, circle, triangle, square"))
y=["red","yellow","orange","green","blue","purple","black"]
if(x=="circle"):
    t.fillcolor(random.choice(y))
    t.begin_fill()
    t.circle(50)
    t.end_fill()
if(x=="triangle"):
    t.fillcolor(random.choice(y))
    t.begin_fill()
    for line in range(3):
        t.right(120)
        t.forward(100)
    t.end_fill()
if(x=="square"):
    t.fillcolor(random.choice(y))
    t.begin_fill()
    for line in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
turtle.done()