print ('Hello')
x=input('Please enter your value: ')
x=float(x)
z=round(x, 0)
if x-z>=0:
	#round down
	if z%2==0:
	#even
        	print(z, 'is the closest even value')

	else:
	#odd
		z=z+1
		print(z, 'is the closest even value')
else:
	#round up

	if z%2==0:
	#even
        	print(z, 'is the closest even value')

	else:
	#odd
		z=z-1
		print(z, 'is the closest even value')
