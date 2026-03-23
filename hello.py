# ask for user's name
name = input("What is your name? ").title().strip()

# split user's name into first and last name
parts = name.split()
first = parts[0]

# print user's first name
print(f"Hello, {first}")