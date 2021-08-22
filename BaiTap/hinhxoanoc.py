import turtle

t = turtle.Turtle()

d = 10

while True:
    t.circle(d, 10)
    t.left(30)
    d +=5
    if t.distance(0,0)  > 100:
        break


turtle.done()
