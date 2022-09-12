import turtle

colors = ['green','orange','red','yellow']

t = turtle.Pen()

turtle.bgcolor('black')  #background color of the window
t.speed(150)

for i in  range(1000):
    t.pencolor(colors[i%4]) #inbuilt function()
    t.width(i//100+1)    
    #t.forward(10)
    
    #t.right(59)
    t.left(120)
    t.forward(i)
    
    
turtle.done()