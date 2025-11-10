'''
This code will generate a graphic drawing like a shell, and the user will 'DIY' the shell by picking the color of the pattern they like. After putting on the color pattern on the shell, the code will ask what color would the user like on some trees as a decoration. So the code will draw the trees with the picked color from the user at the bottom left and the bottom right.
'''
import turtle
t = turtle.Turtle()
t.speed(10)

start = input("Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!").lower().strip()

if start == "start":
    for i in range(70):
        t.forward(5+i)
        t.right(15)
        
t.goto(5)
t.penup()
turtle.done()

color = input("It time to put in some patterns! What color would You like the patterns to be? (orange /pink/ green/ blue)").lower().strip()


def draw_pattern(x, y):
    seasontheme =   {"orange":"#FFB533", "pink":"#FF73C3", "green":"#12C517", "blue":"#4CC9F0"}
    t.color(seasontheme[color])
    
    t.penup()
    t.goto(30 + x, 40 + y)
    t.stamp()
    
    t.penup()
    t.goto(60 + x, 10 + y)
    t.stamp()
    
    t.penup()
    t.goto(90 + x, 40 + y)
    t.stamp()

draw_pattern(-80, -80)
draw_pattern(-110, -20)
draw_pattern(-15, 5)
draw_pattern(15, -65)
draw_pattern(-20, -140)
draw_pattern(-140, -145)
draw_pattern(-200, -55)
draw_pattern(-170, 40)
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
tur.speed(10)

treecolor = input("Lets add some trees for decoration. What color would You like the tree to be? (orange /pink/ green/ blue)").lower().strip()


def draw_treepattern(level, branch_length):
    treetheme =   {"orange":"#FFB533", "pink":"#FCB3F5", "green":"#12C517", "blue":"#BFF5F5"}
    if level > 0:
        tur.forward(branch_length)
        tur.left(40)
        draw_treepattern(level-1, branch_length/1.61)

        tur.right(80)
        draw_treepattern(level-1, branch_length/1.61)
        
        tur.left(40)
        tur.back(branch_length)
        
    else:
        tur.color(treetheme[treecolor])
        tur.stamp()
        tur.color("brown")
        return 
        
def tree_location(x, y, length, depth):
    tur.penup()
    tur.goto(x, y)
    tur.setheading(90) 
    tur.pendown()

    tur.color("brown")
    tur.width(3)
    tur.shape("triangle")
    
    draw_treepattern(depth, length)

tree_location(-150, -330, 80, 5) 
tree_location(150, -330, 80, 5)