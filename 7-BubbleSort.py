iRange = int(input("Please Input Length: ")) + 1

myList=[0 for i in range(iRange)]

for i in range(1,iRange):
    myList[i] = int(input("Input number {}: " .format(i)))

print("The Numbers are: ", end ="")

for i in range(1, iRange):
    print((myList[i]), end = " ")


for i in range(iRange,1,-1 ):

    for j in range(1,i):
        if myList[j] < myList[j-1]:
            b = myList[j-1]
            myList[j-1] = myList[j]
            myList[j]=b

print("\nThe Sorted Numbers are: ", end ="")

for i in range(1, iRange):
    print((myList[i]), end = " ")