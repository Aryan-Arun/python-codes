#import turtle
import turtle

#register screen
screen=turtle.Screen()

#make size of screen
screen.setup(800,600)

#make color of screen
screen.bgcolor("black")

#make pen turtle
pen=turtle.Turtle()

#setting color of pen
pen.color("white")

#making function to create rectangle
def rect(length,width,color):
    #make pen size
    pen.pensize(2)
    #filling color of pen/adding color to pen
    pen.fillcolor(color)
    #start filling of color to pen
    pen.begin_fill()
    #make a loop for 2 times
    for line in range(2):
        #forward 
        pen.forward(length)
        #right 
        pen.right(90)
        #forward
        pen.forward(width)
        #right
        pen.right(90)
    #end filing of pen
    pen.end_fill()
#make another function to move turtle
def move(x,y):
    #lift pen up
    pen.up()
    #tell pen to go to x,y
    pen.goto(x,y)
    #lift pen down
    pen.down()
#calling function/telling turtle to go to -400,-200
move(-400,-200)
#calling function
rect(80,100,"yellow")

#making rect 2
move(-320,-100)
rect(80,400,"yellow")
#making rect 3
move(-240,-150)
rect(80,250,"yellow")
#making rect 4
move(-160,-75)
rect(80,400,"yellow")
#making rect 5
move(-80,-185)
rect(80,400,"yellow")
#making rect 6
move(0,-100)
rect(80,320,"yellow")
#making rect 7
move(80,-200)
rect(80,400,"yellow")
#making rect 8
move(160,-95)
rect(80,400,"yellow")
#making rect 9
move(240,-135)
rect(80,400,"yellow")
#making rect 10
move(320,-110)
rect(80,400,"yellow")



#makeing the moon

pen.up()
pen.goto(320,200)
pen.down()

pen.fillcolor("white")
pen.begin_fill()

pen.circle(50)

pen.end_fill()











    






#finish turtle
turtle.done()