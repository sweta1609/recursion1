def lastIndex(a,x):
    l = len(a)
    if l == 0:
        return -1
    b = a[1:]
    islastIndex = lastIndex(b,x)
    if islastIndex != -1:
        return islastIndex + 1
    if a[0] == x:
        return 0
    else:
        return -1 
   
l = int(input())
a = list(map(int,input().split()))
x = int(input())
print(lastIndex(a,x))
