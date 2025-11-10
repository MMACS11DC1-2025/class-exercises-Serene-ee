#--- Explaination and how to approch the program---

This code will generate a graphic drawing like a shell, and the user will 'DIY' the shell by picking the color of the pattern they like. After putting on the color pattern on the shell, the code will ask what color would the user like on some trees as a decoration. So the code will draw the trees with the picked color from the user at the bottom left and the bottom right. After that, the code will print out the total count of recursive function calls and when the user input 'finish', the program will clear the screen.


#--- Challanges, debugging, testing process, and test case ---

While developing this program, there were many challanges approached.
- No ideas and directions on how to get started
- Need to search up how to draw sprial
- Didn't know how to count the recursive calls(recursive approach below)

Debugging:
- start = input(---) instead of print(---)/n start = input()
- the tree's location: In order to make the tree perpendicular to the ground, I should use tur.setheading() instead of tur.right() or tur.left()

Testing process:
- since the pattern needs to be fitted in the shell, I needed to call draw_pattern many times with different coordinates, so I spent a lot of time on adjusting and testing where the patterns should be to look the best.
- for the trees, I wanted to put them in the shell at first, but I noticed that trees are too big to be put in the shell in a level of 5, so I just put them at bottom left and right as a decoration. And so the location of them also took me time to adjust, espeicaly on how to make them perpendicular to the ground.

Test case:
"Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!"
input: start
(expected: Draw out a shell)
(actual: Draw out a shell)
"It time to put in some patterns! What color would You like the patterns to be? (orange /pink/ green/ blue)"
input: orange
(expected: Draw out orange coloured pattens in the shell)
(actual: Draw out orange coloured pattens in the shell)
"Lets add some trees for decoration. What color would You like the tree to be? (orange /pink/ green/ blue)"
input: green
(expected: Draw out two trees with green leaf)
(actual: Draw out two trees with green leaf, one at the bottom left, one at the bottom right)
"Total Recursive Calls Executed: 126. Please enter 'finish' to end."
input: finish
(expected: Code ended.)
(actual: Cleared the drawing.)


#--- Recursive approach ---

- For my recursive function(trees), I took the one in class materials as an example, where I changed some colors and variable names of it. The most important part, is the location of the trees, which I also spent more time on it. I added length, and depth, along with x and y, and I adjusted the numbers to put them where I want. While adjusting, I also overcomed the challange where I was struggling to make the trees perpendicular to the ground.


#--- How inputs affects outputs ---

- In this program, there are 4 inputs required from the users:
#1 "Hi user, I am a shell DIY bot, in this python, you will be able to create your custom shell! Enter 'start' to get started!"
(For #1, there are no affects because it's just an interaction with users in order to get started.)

#2 "It time to put in some patterns! What color would You like the patterns to be? (orange /pink/ green/ blue)"
(For #2, the user's input would affect which color would the shell's pattern be in the drawing.)

#3 "Lets add some trees for decoration. What color would You like the tree to be? (orange /pink/ green/ blue)"
(for #3, the user's input would affect which color would the tree leaf be in the drawing.)

#4 "Total Recursive Calls Executed: " + str(total_calls) + ". Please enter 'finish' to end."
(For #4, the user's input would lead to clearing the screen at the end of the program.)



#--- Reasonable recursion depth ---

- For my recursion, I think 8 would be too high, because it will be too complex, and though animation will take a long time to draw it out. The depth 2 would be too low, because it's to simple and the drawing won't look like a tree.