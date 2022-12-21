n=int(input())
p=n
s=n*n
sum=0
while s:
    k=s%10
    sum=sum+k
    s=s//10
if sum==p:
    print("Neon Number")
else:
    print("Not Neon Number")
    