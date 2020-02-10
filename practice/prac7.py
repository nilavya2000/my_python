list = [10,10, 20, 4, 99, 45, 99]
list1[20]=[]
for i in list:
	if i not in list:
		list1.append(i)

list1.sort()


print(" ",list1[2])

