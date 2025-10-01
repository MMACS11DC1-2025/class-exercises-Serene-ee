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
    if name in file:
        my_favourites = file.readline().strip().split(",")

    most_sim = 0

for line in file:
    their_favs = line.strip().split(",")
    their_name = their_favs[1]

    common_interest = 0
    top_friend = ""

    for faves in my_favourites:
        if faves in their_favs:top_friend = ""
            common_interest += 1

    if common_interest > most_sim:
        top_friend = their_name
        most_sim = common_interest

print(top_friend)