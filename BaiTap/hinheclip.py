import turtle

t = turtle.Turtle()

d = 100

t.rt(45)

while True:

    t.circle(d, 90)
    t.circle(d / 2, 90)
    t.circle(d, 90)
    t.circle(d / 2, 90)
    t.rt(20)


turtle.done()
