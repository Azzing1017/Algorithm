N = int(input())

cnt = 1
sum = 1
while True:
    sum += cnt*6 - 6
    if N <= sum:
        break
    cnt += 1

print(cnt)