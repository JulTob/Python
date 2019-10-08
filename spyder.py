import turtle

turtle.bgcolor("grey")
turtle.shape("turtle")
turtle.color("red","black")
turtle.pensize(2)
g = (1 + 5 ** 0.5) / 2
for iii in range(0,10):
    for ii in range(0,5):
        for i in range(0,5):
           turtle.forward(100*(g**(iii+1)))
           turtle.right(144)
        turtle.right(1*72)
        for i in range(0,5):
           turtle.forward(100*(g**iii))
           turtle.right(-72)


turtle.exitonclick()
