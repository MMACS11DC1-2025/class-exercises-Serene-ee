#Fractal Generator
#Serene Lee
#Oct 27, 2025

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

import turtle
tur = turtle.Turtle()
def draw_treepattern(level, branch_length, x, y):
  
  seasontheme =	{"autumn":"#FFB533", "spring":"#FCB3F5", "summer":"#12C517", "winter":"#BFF5F5"}
  if level > 0:
    tur.penup()
    tur.goto(30 + x, 40 + y)
    tur.pendown()
    tur.forward(branch_length)
    tur.left(40)
    draw_treepattern(level-1, branch_length/1.61, 30 + x, 40 + y)

    tur.right(80)
    draw_treepattern(level-1, branch_length/1.61, 50 + x, 70 + y)
    
    tur.left(40)
    tur.back(branch_length)
  else:  
    tur.color(seasontheme["spring"])
    tur.stamp()
    tur.color("brown")
    
tur.penup()
tur.goto(0, -180)
tur.left(90)
tur.pendown()

tur.color("brown")
tur.width(3)
tur.shape("triangle")

draw_treepattern(4, 30, -190, 60)