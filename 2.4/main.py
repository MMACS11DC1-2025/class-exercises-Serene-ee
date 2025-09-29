file = open("2.4/responses.csv")
for line in file:
    if "salomi" in line.lower():
        print(line)
