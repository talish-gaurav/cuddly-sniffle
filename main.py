


def cube(x):
    return x**3


n= int(input("Enter the integer you would like to check if it is divisible by your number"))

def check(n):
    if n%3==0:
        print("Your cube number is ",cube(n))

    else:
        print("Not divisible")

check(n)