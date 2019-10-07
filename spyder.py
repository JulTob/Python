import turtle

turtle.bgcolor("grey")
turtle.shape("turtle")
turtle.color("red","black")
turtle.pensize(2)
for iii in range(1,10):
    for ii in range(0,5):
        for i in range(0,5):
           turtle.forward(161*iii//5)
           turtle.right(144)
        turtle.right(1*72)
        for i in range(0,5):
           turtle.forward(100*iii//5)
           turtle.right(-72)


turtle.exitonclick()
