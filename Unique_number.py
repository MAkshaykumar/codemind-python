n=input()
d=[]
for i in n:
    d.append(i)
    if d.count(i)!=1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")