def hello_function():
    print("Hello World")

hello_function()
hello_function()



def compare_function(a,b):
    if a > b:
        print("{} is greater than {}".format(a,b))
    elif a==b:
        print("{} is equal to {}" .format(a,b))
    else:
        print("{} is less than {}".format(a, b))


compare_function(10,2)

x = 5
y = 9
compare_function(x,y)

compare_function(1,1)


def message_function(message,times=1):
    print(message * times)

message_function("haha")
message_function("haha",10)

def keyword_function(a,b=5,c=10):
    print("a is {}, b is {}, c is {}".format(a,b,c))

keyword_function(2,c=20)
keyword_function(3,b=10,c=20)

def vararg_function(a=5,*numbers,**phonebook):
    print("a",a)

    for single_item in numbers:
        print("single_item",single_item)
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(vararg_function(10,1,2,3,Franco = 1123, Kendrikc = 44312, Tiffany = 55313))


def maxim(a,b):
    if a>b:
        return a
    elif a==b:
        return "the numbers are equal"
    else:
        return b

print(maxim(1,2))
print(maxim(4,4))
print(maxim(10,2))


def print_max(x,y):
    '''
    Prints the maximum of two numbers
    :param x: number 1
    :param y: number 2
    The numbers are integers
    :return:
    '''

    x = int(x)
    y = int(y)

    if x > y:
        print(x)
    else:
        print(y)

print_max(10,2)
print(print_max.__doc__)