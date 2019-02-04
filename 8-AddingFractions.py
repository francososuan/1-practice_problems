import math

a = input("Please Input Fraction 1: ")
frac1 = a.split('/')

b = input("Please Input Fraction 2: ")
frac2 = b.split('/')

num1 = int(frac1[0])
den1 = int(frac1[1])

num2 = int(frac2[0])
den2 = int(frac2[1])


print("Fraction 1: {}/{}" .format(num1, den1))
print("Fraction 2: {}/{}" .format(num2, den2))

num3 = int(num1*den2 + den1*num2)
den3 = int(den1 * den2)
b
print("Sum: {}/{}" .format(num3, den3))

if num3 >= den3:
    whole = num3//den3
    num3 = int(num3 % den3)
else:
    whole = 0


gcd = int(math.gcd(num3,den3))

num3 = num3//gcd
den3 = den3//gcd



print("Sum (Lowest Term):{} {}/{}" .format(whole,int(num3), int(den3)))


