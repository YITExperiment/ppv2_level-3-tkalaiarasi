import random
import turtle as t
t.bgcolor("yellow")

caterpillar = t.Turtle()
caterpillar.shape("square")
caterpillar.color("red")
caterpillar.speed(0)
caterpillar.penup()


leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape("leaf", leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.penup()

leaf.speed(0)
def outside_window():
    pass
def game_over():
    pass
def display_score(current_score):
    pass
def place_leaf():
    pass

def start_game():
    golbalgame_started
    if game_started:
        return
    game_started = Ture

    score = 0
    text_turtle.clear()
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caperpillar.showturtle()
    display_score(score)
place_leaf()    
  
