number = 12

guess = int(input('Input a Number: '))

if guess == number:
    print("Congratulations you have guessed the number")
elif guess > number:
    print("A little too high")
elif guess < number:
    print("A little too low")
else:
    print("Invalid Input")


print("Done")

