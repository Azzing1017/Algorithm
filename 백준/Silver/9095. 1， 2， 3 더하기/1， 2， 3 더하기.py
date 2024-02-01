list = [1, 2, 3]
list_put = []

def go(sum, n):
    if sum > n:
        return 0
    elif sum == n:
        return 1
    else:
        now = 0
        for i in range(3):
            now += go(sum+list[i], n)
        return now

T = int(input())
for _ in range(T):
    n = int(input())
    print(go(0, n))