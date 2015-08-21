B=[]
x=1
while x<=1024:
    for i in range(x,1025):
        B.append(i)
        x=x*2
        break
print(B)
