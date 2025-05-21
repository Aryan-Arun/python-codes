import turtle
screen=turtle.Screen()
screen.setup(400,400)
screen.bgcolor("black")
turtle.color("red")
turtle.circle(70)

turtle.up()
turtle.goto(40,100)
turtle.down()
turtle.circle(3)

turtle.up()
turtle.goto(-40,100)
turtle.down()
turtle.circle(3)


turtle.up()
turtle.goto(0,40)
turtle.down()

turtle.setheading(270)

for i in range(18):
    turtle.forward(2)
    turtle.right(10)

turtle.hideturtle()
turtle.done()