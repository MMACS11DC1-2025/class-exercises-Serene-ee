"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
food = ["Chinese", "Japanese", "Mexican", "Spanish", "Italian"]
score = 0

print("Hi, I am a chatbot, what's your name?")
name = input().lower().strip(" !")
print("Nice to meet you, " + name)

print("Let's play a game, where you need to guess what are the top 5 most popular cuisine in 2025. If you guess one right, your score will +1. Enter 'start' to begin the game.")

reply = input().lower().strip(" !")

if reply == "start":
    print("Please type out one movie that you think it's on the podium.")
else:
    print("Sorry, I don't understand what " + reply + " means.")
    
guessed1 = input()
    
if guessed1 in food:
    score = score + 1
    print("Correct! score +1.")
else:
    print("Incorrect!")

print("Please type out another cuisine that you think it's on the podium.")

guessed2 = input()
    
if guessed2 in food:
    score = score + 1
    print("Correct! score +1.")
else:
    print("Incorrect! But it's really good though.")
    
print("What about another cuisine that you think it's on the podium.")

guessed3 = input()
    
if guessed3 in food:
    score = score + 1
    print("Correct! score +1.")
else:
    print("Unfortunately, incorrect!")
    
print("Please type out another cuisine that you think it's on the podium.")

guessed4 = input()
    
if guessed4 in food:
    score = score + 1
    print("Correct! score +1.")
else:
    print("I like that cuisine too! But sorry, incorrect!")
    
print("Please type out your last answer that you think it's the top 5 most popular cuisine in 2025.")

guessed5 = input()
    
if guessed5 in food:
    score = score + 1
    print("Correct! score +1. Here are all the questions, please enter '67' to view your score.")
else:
    print("Incorrect! Here are all the questions, please enter '67' to view your score.")
    
review = input()

if review == "67":
    print("Your score is " + str(score) + ". Thanks for playing!")
else:
    print("Sorry, this is not the right code.")

percent = input()