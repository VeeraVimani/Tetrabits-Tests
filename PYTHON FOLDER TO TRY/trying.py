import pygame
pygame.init()


print("X= 10")
print("Y= 5")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

name = input("What is your name? ")
name = name
question=("Hello, " + name + "!")

for i in range(5):
    print("This is loop number", i)

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You guessed it right!")
else:
    print("Wrong guess! The number was", number)
