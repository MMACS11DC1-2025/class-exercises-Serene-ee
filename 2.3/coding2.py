"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
print("Judge 1's score:")
j1 = float(input())

print("Judge 2's score:")
j2 = float(input())

print("Judge 3's score:")
j3 = float(input())

print("Judge 4's score:")
j4 = float(input())

print("Judge 5's score:")
j5 = float(input())

total = float(j1) + float(j2) + float(j3) + float(j4) + float(j5)
final = total / 5

print(final)

