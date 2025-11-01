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
  t.goto(30 + x, 40 + y)
  t.stamp()
  
  t.penup()
  t.goto(60 + x, 10 + y)
  t.stamp()
  
  t.penup()
  t.goto(90 + x, 40 + y)
  t.stamp()

draw_pattern(-70,105)
draw_pattern(45,70)
draw_pattern(100,-5)
draw_pattern(109,-80)
draw_pattern(88,-160)
draw_pattern(28,-215)
draw_pattern(-80,-245)
draw_pattern(-190,-215)
draw_pattern(-260,-155)
draw_pattern(-290,-85)
draw_pattern(-290,-5)
draw_pattern(-260,60)
draw_pattern(-235,130)