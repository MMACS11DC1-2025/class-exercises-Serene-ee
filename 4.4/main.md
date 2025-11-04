import turtle
t = turtle.Turtle()

start = input("Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!").lower().strip()

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

color = input("It time to put in some patterns! What color would You like the patterns to be? (orange /pink/ green/ blue)").lower().strip()

def draw_treepattern(level, branch_length):
  
  seasontheme =	{"orange":"#FFB533", "pink":"#FCB3F5", "green":"#12C517", "blue":"#BFF5F5"}
  if level > 0:
    tur.forward(branch_length)
    tur.left(40)
    draw_treepattern(level-1, branch_length/1.61)

    tur.right(80)
    draw_treepattern(level-1, branch_length/1.61)
    
    tur.left(40)
    tur.back(branch_length)
  else:  
    tur.color(seasontheme[color])
    tur.stamp()
    tur.color("brown")
    
tur.penup()
tur.goto(-20, -70)
tur.left(90)
tur.pendown()

tur.color("brown")
tur.width(3)
tur.shape("triangle")

draw_treepattern(4, 30)