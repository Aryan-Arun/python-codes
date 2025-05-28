import turtle
import random
screen=turtle.Screen()
screen.setup(800,800)
screen.bgcolor("black")

t=turtle.Turtle()
t.speed(0) 

def circle():
    colors=["red","blue","green","white","yellow","brown","purple","orange"]
    t.color(random.choice(colors))
    t.begin_fill()
    t.circle(random.randint(5,30))
    t.end_fill()


for i in range(50):
    t.up()
    y=random.randint(-400,400)
    x=random.randint(-400,400)
    t.goto(x,y)
    t.down()
    circle()



turtle.done()