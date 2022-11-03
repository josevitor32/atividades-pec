from turtle import *


def quadrado():
    pendown()
    begin_fill()

    for side in range(1):
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
    end_fill()
    penup()

color('WhiteSmoke')
bgcolor('MidnightBlue')

quadrado()
done()

