#bigggest number in set of numbers

#print ('Please enter your set of 10 values')

'''

a= input (print('a='))

a=float(a)



b= input (print('b='))

b=float(b)



c= input (print('c='))

c=float(c)



d= input (print('d='))

d=float(d)



e= input (print('e='))

e=float(e)



f= input (print('f='))

f=float(f)



g= input (print('g='))

g=float(g)



h= input (print('h='))

h=float(h)



i= input (print('i='))

i=float(i)



j= input (print('j='))

j=float(j)

'''



#a; b; c; d; e = input (print('Enter first five values separated by spaces'))



#a=12;b=6;c=14;d=34;e=46;f=67;g=34;h=73;i=143;j=90

a=[12,336,14,34,46,67,34,73,143,90]

print ('You entered the following values:', a)
x=0
amax=a[x]
x=x+1 #makes value first of following
i=range(1,10)

for num in i:

    if amax<a[x]:

        amax=a[x]
	x=x+1
    else:
	x=x+1
print (amax)
