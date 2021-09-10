import turtle

t = turtle.Turtle()

def ve_cay():
    t.penup()
    t.goto(100,-30)
    t.pendown()

    t.color("green")
    t.begin_fill()

    angle_1 = [60,120,120,]

    for i in angle_1:
        t.rt(i)
        t.fd(100)
    t.rt(150)

    t.end_fill()
    t.penup()

    t.fd(200)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for i in range(2):
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(113)
    t.end_fill()
    turtle.done()

def ve_nha():
    t.penup()
    t.goto(-200, -100)
    t.pendown()

    t.fillcolor("blue")
    t.begin_fill()
    t.goto(-130, -100)
    t.goto(-130, -200)
    t.goto(-200, -200)
    t.goto(-200, -100)
    t.end_fill()

    # ve cua

    t.penup()
    t.goto(-180, -200)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.goto(-180, -150)
    t.goto(-150, -150)
    t.goto(-150, -200)
    t.goto(-180, -200)
    t.end_fill()

    t.penup()
    t.goto(-130, -200)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.goto(-130, -100)
    t.goto(-50, -60)
    t.goto(-50, -160)
    t.goto(-130, -200)
    t.end_fill()

    t.penup()
    t.goto(-110, -160)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    t.goto(-110, -140)
    t.goto(-90, -130)
    t.goto(-90, -150)
    t.goto(-110, -160)
    t.end_fill()

    # ve mai nha
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.goto(-165, -50)
    t.goto(-130, -100)
    t.goto(-200, -100)
    t.end_fill()

    t.goto(-165, -50)
    t.fillcolor("orange")
    t.begin_fill()
    t.goto(-85, -10)
    t.goto(-50, -60)
    t.goto(-130, -100)
    t.goto(-165, -50)
    t.end_fill()

    t.penup()
    t.goto(150, -200)
    t.pendown()


a = ve_nha()

b = ve_cay()