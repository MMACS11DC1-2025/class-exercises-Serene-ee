"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
file = open('2.4/responses.csv')
junk = file.readline()

print("Please input your name for us to search up your information in the database.")
 
name = input()

for line in file:
    if name in line:
        my_favourites = line.strip().split(",")

top_friend = ""
top_score = 0
their_favs = ""
their_name = ""

file = open('2.4/responses.csv')
# get everyone's favourite

for line in file:
    score = 0
    their_favs = line.strip().split(",")
    if my_favourites[2] == their_favs[2]:
        score += 1
    if my_favourites[3] == their_favs[3]:
        score += 1
    if my_favourites[4] == their_favs[4]:
        score += 1
    if my_favourites[5] == their_favs[5]:
        score += 1
    if my_favourites[6] == their_favs[6]:
        score += 1
    if my_favourites[7] == their_favs[7]:
        score += 1
    if my_favourites[8] == their_favs[8]:
        score += 1
    if my_favourites[9] == their_favs[9]:
        score += 1
    # ppl's name
    their_name = their_favs[1]

    # see who's favourite matches user the most
    #for faves in my_favourites:
        #if faves in their_favs:
            #score += 1
    if their_name == my_favourites[1]:
        score = 0

    if score > top_score:
        top_friend = their_name
        top_score = score

print(top_friend)