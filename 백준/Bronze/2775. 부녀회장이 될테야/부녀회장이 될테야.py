T = int(input())
list_a = [[] for _ in range(15)]

for i in range(1, 15):
    list_a[0].append(i)

for i in range(1, 15):
    for j in range(1, 15):
        list_a[i].append(sum(list_a[i-1][:j]))

for _ in range(T):
    k = int(input())
    n = int(input())
    print(list_a[k][n-1])