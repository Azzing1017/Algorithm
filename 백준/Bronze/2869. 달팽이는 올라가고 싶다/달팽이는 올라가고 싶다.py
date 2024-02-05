A, B, V = map(int, input().split())
n = V // (A-B) - A
if n < 0:
    n = 0
V = V - (A-B) * n
while True:
    n += 1
    V -= A
    if V <= 0:
        break
    else:
        V += B

print(n)