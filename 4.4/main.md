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

####

import turtle

t = turtle.Turtle()

print("Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!")
start = input().lower().strip()

if start == "start":
  for i in range(70):
  	t.forward(5+i)
  	t.right(15)
    
t.goto(5)
t.penup()
turtle.done()

def draw_pattern(x, y):
  t.penup()
  t.goto(30 + x, 30 + y)
  t.stamp()
  
  t.penup()
  t.goto(50 + x, 10 + y)
  t.stamp()
  
  t.penup()
  t.goto(70 + x, 30 + y)
  t.stamp()

draw_pattern(-80,100)
draw_pattern(-10,100)
draw_pattern(40,60)
draw_pattern(90,40)
draw_pattern(120,20)
draw_pattern(140,0)