arr = list(map(int, input().split()))
tf = True

for ar in arr:
    if ar == 9:
        tf = False
        break

if tf:
    print("S")
else:
    print("F")