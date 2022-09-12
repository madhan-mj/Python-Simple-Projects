#Make Changes in the angles and play with the code

import turtle

colors = ['red','blue','green','yellow','orange','white']

t = turtle.Pen()
turtle.bgcolor('black')
t.speed(500)

for i in range(1000):
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    #t.forward(90)
    
    t.forward(i)
    t.forward(50)
    t.right(60)
    
    #t.pencolor(colors[i%6])
    #t.width(i//100+1)
    #t.forward(90)   
    #t.forward(i)
    
turtle.exitonclick()