import turtle

colors = ['red','yellow','orange','purple']

t= turtle.Pen()
t.speed(300)
for i in range (1):
    t.pencolor(colors[i%4])
    t.forward(150)
    t.left(55)
    t.forward(45)
    t.right(55)
    t.forward(50)
    t.right(55)
    t.forward(50)
    t.left(55)
    t.forward(35)
    t.left(50)
    t.forward(40)
    t.left(80)
    t.forward(55)
    t.left(48)
    t.forward(45)
    t.right(48)
    t.forward(70)
    t.left(50)
    t.forward(160)
    t.left(48)
    t.forward(75)
    t.right(48)
    t.forward(95)
    t.left(55)
    t.forward(50)
    t.left(75)
    t.forward(40)
    t.left(48)
    t.forward(10)
    t.left(55)
    t.forward(50)
    t.right(53)
    t.forward(50)    
    t.right(53)
    t.forward(45)
    t.right(120)
    t.pencolor('white')
    t.forward(20)
    t.pencolor('red')
    t.right(100)
    t.circle(30)
    t.pencolor('white')
    t.right(87)
    t.forward(20)
    t.forward(170)
    t.pencolor('red')
    t.right(85)
    t.circle(30)
    t.pencolor('white')
    t.right(15)
    t.backward(110)
    t.pencolor('red')
  
  #Window 

    t.left(45)
    t.forward(50)
    
    t.right(125)
    t.forward(110)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.backward(80)
    t.pencolor('white')
    t.backward(10)
    
    t.pencolor('red')
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(110)
    t.right(135)
    t.forward(55)
    t.right(45)
    t.forward(70)
    t.backward(20)
    
turtle.done()