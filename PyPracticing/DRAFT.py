# creating condition to input validation in required range
from cs50 import get_int

n = 0

while n < 1 or n > 8:
       n = get_int("height :")

# printing a hash plus one more hash on each iteration created
for i in range(n):
    for j in range(1, n+1):
        if j > n-i-1 and j < n+1:
            print("#", end="")
        else:
            print(" ", end="")
    print()