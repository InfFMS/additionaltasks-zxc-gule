import math
m=int(input())
p = int(m**0.5)
while m%(p**2)!=0:
    p -= 1
print(p**2)


