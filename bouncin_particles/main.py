'''
BOUNCING BALL
Julio Toboso
Basic program for BOUNCING BALL simulation.
Practice for coding games.
'''

# Imports #
import turtle
import random
#---------#
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(3)

balls = []
for _ in range(20):
    balls.append(turtle.Turtle())

colors = ["blue", "red", "green", "yellow", "orange", "white","purple"]
shapes = ["circle", "triangle", "square"]
for ball in balls:
    ball.shape(
        random.choice(shapes))
    ball.color(
        random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-200,200)
    y = random.randint(-20,20)
    ball.goto(x,200+y)
    ball.dy = random.randint(-5,5)
    ball.dx = random.randint(-5,5)
    ball.da = random.randint(-10,15) # angle


gravity = 0.3

while True:
    wn.update()
    for ball in balls:

        ball.sety(
            ball.ycor() + ball.dy)
        ball.setx(
            ball.xcor() + ball.dx)
        ball.rt(ball.da)
        # Bounce?
        if ball.ycor() < -270:
            ball.dy *= -1
            ball.da *= -1
        else:
            ball.dy -= gravity
            ball.da *= 0.999
        # Wall collision
        if ball.xcor() < -270 or ball.xcor() > 270 :
            ball.dx *= -1
            ball.da *= -1.5



wn.mainloop()
