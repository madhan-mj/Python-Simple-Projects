#MAke Changes with the angles and look for difference in ur output

import turtle

loadWindow = turtle.Screen()
colors = ['red','green','orange','white','yellow','aqua']

t = turtle.Pen()
t.speed(20)
turtle.bgcolor('black')

for i in range(30):
    t.pencolor(colors[i%6])
    t.width(i//100+2)
    t.circle(5*i)
    #t.circle(-5*i)
    t.left(i)

turtle.exitonclick()