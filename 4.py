import random

x=0
y=0
z=1
B=[]

while z<=10:
	y=random.randint(-5,5)
	if y==x:
		print ('repeating value')
	else:
		print('x=', x)
		B.append(x)
		x=y
		z=z+1
print('finished')
print(B)
