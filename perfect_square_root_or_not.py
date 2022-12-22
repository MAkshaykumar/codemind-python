import math

n=int(input())
p=int(math.sqrt(n))
k=p*p
if k==n:
    print("True")
else:
    print("False")