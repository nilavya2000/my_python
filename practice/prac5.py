n=int(input("enter "))
a = [ input() for i in range(n)]
max=a[0]
min=a[0]
c=0
d=0
for i in a:
	if max>i:
		max=i
	elif min<i:
		min=i
for j in a:
	if max==j:
		c=c+1
	elif min==j:
		d=d+1
print(c, d, end='') 
