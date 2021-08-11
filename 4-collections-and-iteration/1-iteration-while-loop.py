# WHILE LOOP
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# PRINT LIST ITEMS
beverages = ["water", "juice", "soda", "tea", "coffee"]
index = 0
while index < len(beverages):
    print(beverages[index])
    index += 1

# BREAK STATEMENT
beverages = ["water", "juice", "soda", "tea", "coffee"]
index = 0
while index < len(beverages):
	print(beverages[index])
	index += 1
	if beverages[index] == "soda":
		print("I found the soda!")
		break

# GUESSING GAME
import random
num = random.randint(1, 5)
guess = int(input("Guess a number from 1 to 5!"))
while guess != num:
    guess = int(input("Wrong guess. Try again!"))
print("You guessed it correctly!")

# PRACTICE
num = random.randint(1, 10)
counter = 1
guess = int(input("Guess a number from 1 to 10!"))
while counter < 3:
    if guess != num:
        if guess < num:
            guess = int(input("Your guess is smaller than the actual number."))
        if guess > num:
            guess = int(input("Your guess is greater than the actual number."))
    else:
        print("You guessed it correctly!")
        break
    counter = counter + 1
print("Your chances have expired!")
