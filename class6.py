import turtle

screen=turtle.Screen()
screen.setup(800,800)
screen.bgcolor("light blue")

pen=turtle.Turtle()
pen.color("black")

pen.up()
pen.goto(-350,-150)
pen.down()

pen.fillcolor("black")
pen.begin_fill()

for square in range(4):
    pen.forward(150)
    pen.right(90)

pen.end_fill()

pen.fillcolor("cyan")
pen.begin_fill()


for triangle in range(3):
    pen.forward(150)
    pen.left(120)

pen.end_fill()

pen.up()
pen.goto(-275,-300)
pen.down()

pen.fillcolor("white")
pen.begin_fill()



for square in range(2):
    pen.forward(20)
    pen.left(90)
    pen.forward(50)
    pen.left(90)


pen.end_fill()




pen.up()
pen.goto(300,300)
pen.down()


pen.fillcolor("yellow")
pen.begin_fill()

pen.circle(50)

pen.end_fill()


pen.up()
pen.goto(-400,-300)
pen.down()

pen.fillcolor("green")
pen.begin_fill()

pen.forward(1500)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(1500)
pen.right(90)
pen.forward(100)
pen.right(90)

pen.end_fill()






    


turtle.done()