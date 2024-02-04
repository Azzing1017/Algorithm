N = int(input())
a = N // 5
b = N % 5
while True:
    if b % 3 != 0:
        if a == -1:
            break
        a -= 1
        b += 5
    else:
        break

if a == -1:
    print(-1)
else:
    print(a + b//3)