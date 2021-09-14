s=1
arr = []
print("put array size ")
n = int(input())
print("put the array",s,"value ")
x = int(input())
arr.append(x)
for s in range(0,n-1):
    if s<n:
        s += 1
        print("put the array",s+1, "value")
        x = int(input())
        arr.append(x)
print(arr)



    

