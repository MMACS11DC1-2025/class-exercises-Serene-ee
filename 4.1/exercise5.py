#Serene Lee
#date:Oct 15
#exercise 5

import turtle
t = turtle.Turtle()

while True:
    command = input("Type 'smile' to draw a smile.")

    if command == "smile":
        def smile(x, y):
            t.circle(90)
            t.penup()
            
            t.goto(40, 120)
            t.stamp()
            t.goto(-30, 120)
            t.stamp()
            
            
            t.goto(-50, 70)
            t.stamp()
            t.goto(-30, 60)
            t.stamp()
            t.goto(-10, 50)
            t.stamp()
            t.goto(10, 50)
            t.stamp()
            t.goto(30, 60)
            t.stamp()
            t.goto(50, 70)
            t.stamp()
    
    else:
        break

smile(0, 0)
smile(100, 110)
smile(250, 100)