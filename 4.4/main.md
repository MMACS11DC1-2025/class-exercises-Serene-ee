import turtle
# Initialize the shell
t = turtle.Turtle()

# Set the turtle drawing speed, to draw the shell more efficiently
t.speed(10)

# Ask the user for interaction to start drawing the shell
start = input("Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!").lower().strip()

# --- Shell Drawing ---
if start == "start":
    # Loop 70 times to draw the expanding spiral
    for i in range(70):
        t.forward(5+i)
        t.right(15)

# After the spiral loop, move turtle to the middle to form a shell shape        
t.goto(5)
# Lift the pen to stop the drawing
t.penup()
turtle.done()

# --- Pattern ---
# Ask the user for a color choice for the decorative patterns for the 'shell'
color = input("It time to put in some patterns! What color would You like the patterns to be? (orange /pink/ green/ blue)").lower().strip()

# Define a function to make the three stamps a group
def draw_pattern(x, y):

    # Dictionary for patterns colors
    seasontheme =   {"orange":"#FFB533", "pink":"#FF73C3", "green":"#12C517", "blue":"#4CC9F0"}
    # Set the turtle color based on the user's input
    t.color(seasontheme[color])
    
    # stamp the first pattern
    t.penup()
    t.goto(30 + x, 40 + y)
    t.stamp()
    
    # stamp the second pattern
    t.penup()
    t.goto(60 + x, 10 + y)
    t.stamp()
    
    # stamp the third pattern
    t.penup()
    t.goto(90 + x, 40 + y)
    t.stamp()

# --- Pattern Drawing ---
# draw the patterns by calling draw_pattern multiple times with different (x, y) coordinates
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

# --- Tree ---
import turtle
# Initialize the trees
tur = turtle.Turtle()

# Set the turtle drawing speed, to draw the trees more efficiently
tur.speed(10)

# Ask the user for a color choice for the tree leafs
treecolor = input("Lets add some trees for decoration. What color would You like the tree to be? (orange /pink/ green/ blue)").lower().strip()

# Define a recursive function to draw the trees 
def draw_treepattern(level, branch_length):
    # Dictionary for leaf colors
    treetheme =   {"orange":"#FFB533", "pink":"#FCB3F5", "green":"#12C517", "blue":"#BFF5F5"}

    # Base Case
    if level <= 0:
        # Set the turtle color based on the user's input
        tur.color(treetheme[treecolor])
        # Stamp the leaf
        tur.stamp()
        tur.color("brown")
        return 1 
    
    else:
        # Start counting this current call
        current_calls = 1 
        
        tur.forward(branch_length)
        tur.left(40)
         # Call function recursively and add the returned count
        current_calls += draw_treepattern(level-1, branch_length/1.61) 

        tur.right(80)
        # Call function recursively and add the returned count
        current_calls += draw_treepattern(level-1, branch_length/1.61)
        
        tur.left(40)
        tur.back(branch_length)
        
        # Return the total count
        return current_calls

# --- Tree location ---
def tree_location(x, y, length, depth):
    tur.penup()
    tur.goto(x, y)
    # Set heading perpendicular to the ground
    tur.setheading(90) 
    tur.pendown()

    tur.color("brown")
    tur.width(3)
    tur.shape("triangle")
    
    # Start the recursive drawing and return the total count received.
    return draw_treepattern(depth, length)

# Draw the first tree at bottom left
count1 = tree_location(-150, -330, 80, 5) 

# Draw the second tree at bottom right
count2 = tree_location(150, -330, 80, 5)

# Add the calls together from both trees
total_calls = count1 + count2
# Tell the user the final recursive calls
calls = input("Total Recursive Calls Executed: " + str(total_calls) + ". Please enter 'finish' to end.")

# Clear the screens if the user enters 'finish'
if calls == "finish":
  t.clear()
  tur.clear()