n = int(input())
s=0
if n<=9:
	for i in range(0,n+1):
		s+=i*(10**(n-i))
	print(s)
else:
	for i in range(0,n):
                s+=i*(10**((n-i)+1))
	print(s)
	print("!!!!!!!!!!")
