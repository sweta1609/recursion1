def sumArray(arr):
    # Please add your code here
    pass
    n = len(arr)
    if n == 0:
        return 0
    b = arr[1:]
    issumarray = sumArray(b)
    output = arr[0] + issumarray
    return output
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
