import random

z=0 #zero
v=0 #total value
B=[]

while v<30:
	x=random.randint(0,8)
	B.append(x)
	if x==0:
		z=z+1
		if z==3:
			print('3 zeroes')
			break
	v=v+1
print('finished')
print(B)
