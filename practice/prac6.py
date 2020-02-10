n = int(input())
arr = list(map(int, input().split()))
b=[]
for i in arr:
	if i not in arr:
		b.append(i)
b.sort()
print(b[:-2])

