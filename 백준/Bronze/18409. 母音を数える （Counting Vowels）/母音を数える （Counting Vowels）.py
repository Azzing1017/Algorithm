N = int(input())

cnt = 0
for i in input().strip():
    if i in ['a', 'e', 'o', 'u', 'i']:
        cnt += 1

print(cnt)
