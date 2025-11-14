"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""

total = 0

print("Hi, would you like a burger for $5? (Yes/ No)")

burger = input().lower().strip()

if burger == "yes":
    total += 5
else:
    total += 0

print("Hi, would you like fries for $3? (Yes/ No)")

fries = input().lower().strip()

if fries == "yes":
    total += 3
else:
    total += 0

tax = int(total)*float(0.14)
final = tax + int(total)

print("Your total is $" + str(final) + " dollars.")