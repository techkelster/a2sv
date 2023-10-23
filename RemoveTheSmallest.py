tests = int(input())
i = 0
while i < tests:
    leng = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    j = 0
    while j < (len(arr) - 1):
        if abs(arr[j] - arr[j + 1]) <= 1:
            arr.pop(j)
        else:
            j += 1  
    if len(arr) == 1:
        print("YES")
    else: 
        print("NO")
    i += 1
