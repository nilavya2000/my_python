def miniMaxSum(arr):
    s=[5]
    for i in s:
        sum=0
        for j in arr:
            if j==i:
		
            else:
                sum+=arr[j]
        s[i]=sum    
    min=s[0]
    max=s[0]
    for i in range(1,5):
        if min>s[i]:
            min=s[i]
        if max<s[i]:
            max=s[i]
    print(min, " ",max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

