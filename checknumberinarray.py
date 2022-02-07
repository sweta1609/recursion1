def checkNumber(arr, x):
    # Please add your code here
    pass
    n = len(arr)
    if n == 0:
        return False
    if arr[0] == x:
        return True
    b = arr[1:]
    ischecknumber = checkNumber(b,x)
    if ischecknumber:
        return True
    else:
        return False

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
