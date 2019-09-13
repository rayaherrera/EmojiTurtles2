import turtle
ray1=turtle
ray1.bgcolor("black")
ray1.color("yellow")
ray1.begin_fill()
ray1.circle(120)
ray1.end_fill()

import turtle
ray2=turtle
ray2.color("black")
ray2.penup()
ray2.left(90)
ray2.forward(150)
ray2.left(90)
ray2.forward(30)
ray2.pendown()
ray2.forward(50)

import turtle
ray3=turtle
ray3.color("blue")
ray3.penup()
ray3.left(180)
ray3.forward(90)
ray3.right(90)
ray3.pendown()
ray3.begin_fill()
ray3.circle(25)
ray3.end_fill()

import turtle
ray4=turtle
ray4.color("deep pink")
ray4.penup()
ray4.forward(100)
ray4.left(90)
ray4.forward(25)
ray4.right(180)
ray4.pendown()
ray4.forward(80)

turtle.exitonclick()

