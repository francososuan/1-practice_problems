password = 100;
x=1


while x == 1:
    guess = int(input("Please Enter Password: "))

    if guess == password:
        x=0
        print("You have guessed the Password")
    elif guess >password or guess <password:
        print("Try Again")


print("Done")

checker = True

while checker:
    s = input("Enter a string: ")
    if s == "quit":
        break
    print("Length of the string is ", len(s))

print("Done")
