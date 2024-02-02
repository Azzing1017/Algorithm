N = int(input())

def fac(i):
    if i == 0:
        return 1
    else:
        res = i * fac(i-1)
        return res

print(fac(N))