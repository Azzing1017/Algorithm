def solve(n, m):
    if max(n, m) % min(n,m) == 0:
        if min(n, m) == n:
            return "factor"        
        elif max(n, m) == n:
            return "multiple"
    else:
        return "neither"

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        print(solve(n, m))