def power_n(a,b):
    if a == 0 and b == 0:
        return 1
    smalloutput = a**b
    return smalloutput
a,b = input().split()
a = int(a)
b = int(b)
print(power_n(a,b))
