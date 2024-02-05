N = int(input())
li = [list(map(int, (input()).split())) for n in range(N)]

for i in li:
    num = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            num += 1
    i.append(num)

print(*[val[2] for val in li])