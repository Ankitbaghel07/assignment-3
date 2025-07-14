# calculate the factorial using function
#defining function
def factorial(a):
    if (a<2):
        return 1
    else:
        return a*(factorial(a-1))
# take input from user
a=int(input("enter a number: "))

result= factorial(a)
print(f"factorial of {a} is: {result}")

        