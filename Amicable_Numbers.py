def num(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
            
    return sum
a=int(input())
b=int(input())
if num(a)==num(b):
    print("Amicable")
else:
    print("Not Amicable")