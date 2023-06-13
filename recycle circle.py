def draw_circle(size,angle,shift):
    turtle.bgcolour(next(colors))
    tutle.circle(size)
    draw_circle(size+5)

turtle.bgcolor("black")
turtle.speed("fast")
turtle.pensize(40)
draw_circle(30)
