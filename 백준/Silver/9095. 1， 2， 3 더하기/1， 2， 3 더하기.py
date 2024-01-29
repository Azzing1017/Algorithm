list = [1, 2, 3]
list_put = []

def go(n):
    global list, list_put, count
    if sum(list_put) > n:
        return
    elif sum(list_put) == n:
        count += 1
        return
    else:
        for i in list:
            list_put.append(i)
            go(n)
            list_put.pop()

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    go(n)
    print(count)