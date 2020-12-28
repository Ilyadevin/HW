from turtle import Turtle, Screen
import math
COLORS = ["red", "yellow", "blue", "brown", "pink", "green", "black", "orange", "purple"]


def draw_polygons(sides, area):
    for i, sd in enumerate(range(sides, 2, -1)):
        side_length = math.sqrt(area / sd * 4 * math.atan(math.pi / sd))
        a_color = COLORS[i % len(COLORS)]
        rest.fillcolor(a_color)
        rest.pendown()
        rest.begin_fill()
        for _ in range(sd):
            rest.forward(side_length)
            rest.left(360 / sd)
        rest.end_fill()
        rest.penup()
        rest.forward(side_length / 2)
        rest.right(30)


wn = Screen()
rest = Turtle()
rest.speed('fastest')
draw_polygons(20, 40_000)
rest.hideturtle()
wn.exitonclick()