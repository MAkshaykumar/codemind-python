a=int(input())
cnt=0
for i in range(1,a+1):
    if (a%i==0):
        cnt=cnt+1
if cnt==2:
    print("prime")
else:
    print("not a prime")