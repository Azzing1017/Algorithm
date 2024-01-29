N = int(input())
def digit(N, c):
    if N < 10**c:
        result = 0
        for i in range(1, c):
            result = result + (i * 9 * 10**(i-1))
        M = N - 10**(c-1) + 1
        result = result + M*c
        return result
    else:
        return digit(N, c+1)

print(digit(N, 1))