import random

low = 1
high = 20

answer = random.randint(low, high)
count = 0

print("Python Number guessing game")

while True:
    guess = (input("Select a number between 1 and 20: "))

    if guess.isdigit():
        guess = int(guess)
        count += 1

        if guess < low or guess > high:
            print("Number is out of range")
        elif guess > answer:
            print("Too high!! Try again!")
        elif guess < answer:
            print("Too low!! Try again!")
        else:
            print(f"Correct guess!! it's {answer}")
            print(f"Number of guess {count}")
            break
    else:
        print("Correct guess!!")
        print(f"Select a number between {low} and {high}")


