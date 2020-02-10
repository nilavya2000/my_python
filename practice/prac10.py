def time(s):
	if s[-2:]=="am" and s[:2]=='12':
		return "00" + s[2:-2]
	elif s[-2:]=="am":
		return s[:-2]
	elif s[-2:]=="pm" and s[:2]=='12':
		return s[:-2]
	else :
		return str(int(s[:2]) + 12) + s[2:8]

s=input("time: ")
print(time(s))
