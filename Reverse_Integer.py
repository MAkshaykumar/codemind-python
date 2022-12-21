def revs(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if n<0:
    print(-revs(abs(n)))
else :
    print(revs(n))
    