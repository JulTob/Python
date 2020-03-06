# Analog clock
#- By JulioTbs


import turtle
# siriusly?!
#- Yeah, as a GUI
# Yeah, but... why?
#- Shut up

import time



wn = turtle.Screen()
# You can call it "window", you know?
#- Shut up!


wn.bgcolor("black")
wn.setup(width=350, height=350)
wn.title("Clock")
wn.tracer(0)

def newPen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    return pen

pen_clock = newPen()
pen_m = newPen()
pen_s = newPen()
pen_h = newPen()





def draw_clock(pen):
    # Draw clock face
    pen.up()
    pen.goto(0, 115)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(120)

    # Hour marks
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(110)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,-5)
        pen.rt(30)

def draw_second(pen, s=0):
    # draw seconds
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (s/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

def draw_minute(pen, m = 0):
    # draw minute
    pen.penup()
    pen.goto(0,0)
    pen.color("grey")
    pen.setheading(90)
    angle = (m/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

def draw_hour(pen, h = 0):
    # draw hour
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h/12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)






def tick(check= True):
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    if check:
        if m < 2:   # Don't overload the system, man
            pen_h.clear()
            draw_hour(pen_h, h)
        if s < 2:   # Whoyugonacall? Safeguards!
            pen_m.clear()
            draw_minute(pen_m, m)
    else:
        draw_hour(pen_h, h)
        draw_minute(pen_m, m)



    time.sleep(1)
    pen_s.clear()
    draw_second(pen_s, s)

    wn.update()


draw_clock(pen_clock)

tick(False)

while(True):
    tick()
wn.mainloop()
