"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
file = open("responses.csv")
junk = file.readline()

print("Please input your name for us to search up your information in the database.")
 
name = input()

if name in file.readline():
    my_favourites = file.readline().strip().split(",")

most_sim = 0
top_friend = ""

for line in file:
    their_favs = line.strip().split(",")
    their_name = their_favs[1]

    common_interest = 0

    for faves in my_favourites:
        if faves in their_favs:
            common_interest += 1

    if common_interest > top_score:
        top_friend = their_name
        top_score = common_interest

print(top_friend)