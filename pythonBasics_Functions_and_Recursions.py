# Functions in python
# 1. Basic addition function
def sum(a,b):
    return a + b

# print(sum(10,35))


# Recursion Basic: Recursion function which calls itself .

def recFunction(n):
    if(n==0):  # Base Case
        return
    print(n)
    recFunction(n-1)

recFunction(5)