def firstIndex(arr, x,si):
    # Please add your code here
    pass
    n = len(arr)
    if si == n:
        return -1
    if arr[si] == x:
        return si
    isfirstIndex = firstIndex(arr,x,si+1)
    return isfirstIndex
    
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
