from turtle import *


def drawPlanet(planetSize, planetColour):    
    color(planetColour)
    pendown()
    begin_fill()

    for side in range(360):
        left(1)
        forward(planetSize)
    end_fill()
    penup()

speed(11)
bgcolor('MidnightBlue')

drawPlanet(1, 'Red')
forward(200)
drawPlanet(1, 'White')
left(120)
forward(250)
drawPlanet(1, 'Green')
hideturtle()
done()

