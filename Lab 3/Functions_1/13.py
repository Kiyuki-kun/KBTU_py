import random

print("Hello! What is your?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
numb = random.randint(0,20)
count = 0
while(True):
    guess = int(input("Take a guess: "))
    count += 1
    if (guess > numb):
        print("Your guess is too high.")
    elif (guess < numb):
        print("Your guess is too low.")
    else:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        break
    
    