import turtle as t

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    
for counter in range(1,3):
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
t.end_fill()
t.penup()
t.speed("slow")
t.bgcolor("dodger blue")
#feet
t.goto(-100,-150)
rectangle(50,20,"navy")
t.goto(-30,-150)
rectangle(50,20,"navy")
#legs
t.goto(-25,-50)
rectangle(15,100,"maroon")
t.goto(-55,-50)
rectangle(-15,100,"maroon")
#body
t.goto(-90,100)
rectangle(100,150,"forestgreen")
#arms
t.goto(-150,70)
rectangle(60,15,"peru")
t.goto(-150,110)
rectangle(15,40,"peru")

t.goto(10,70)
rectangle(60,15,"peru")
t.goto(55,110)
rectangle(15,40,"peru")
#neck
t.goto(-50,120)
rectangle(15,20,"grey")
#head
t.goto(-85,170)
rectangle(80,50,"gold")


