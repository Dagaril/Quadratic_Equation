import random

s=0
v=0
B=[]

while 1:
	x=random.randint(0,10)
	s=s+x
	if s<50:
		v=v+1
		if v==10:
			B.append(x)
			break
		else:
			B.append(x)
	else:
		break
print('finished')
print(B)
z=sum(B)
print('sum=',z)
