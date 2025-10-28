#Fractal Generator
#Serene Lee
#Oct 27, 2025

import turtle
t = turtle.Turtle()

def draw_tree(level, branch_length):
  if level > 0:
    
    turtle.forward(branch_length)
    turtle.left(40)
    draw_tree(level-1, branch_length/1.61)
    
    turtle.right(80)
    draw_tree(level-1, branch_length/1.61)
    
    turtle.left(40)
    turtle.back(branch_length)
    
  else:
    turtle.color("green")
    turtle.stamp()
    turtle.color("brown")
    
turtle.speed()
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")

draw_tree(2, 120)