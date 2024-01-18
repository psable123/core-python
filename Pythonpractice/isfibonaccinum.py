import math

def isPerfectSquare(n):
    root = int(math.sqrt(n))
    print(root)
    return root*root == n

def isFibonacciNumber(n):
    if isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4):
        return True
    else:
        return False
n = 13
if isFibonacciNumber(n):
    print(n,"is a fibonaaci number")
else:
    print(n,"is not a fibonaaci number")

