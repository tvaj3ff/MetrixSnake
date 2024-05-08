import turtle as t
from move import *

brd = t.Screen()
brd.title("Snake Game")
brd.bgcolor("blue")
# the width and height can be put as user's choice
brd.setup(width=600, height=600)
brd.tracer(0)

brd.listen()
brd.onkeypress(group, "Up")
brd.onkeypress(go_down, "Down")
brd.onkeypress(go_left, "Left")
brd.onkeypress(go_right, "Right")
