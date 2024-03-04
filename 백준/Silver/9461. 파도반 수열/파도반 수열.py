pn = [0]*101
pn[1] = 1
pn[2] = 1
pn[3] = 1
pn[4] = 2
for i in range(5, 101):
    pn[i] = pn[i-1]+pn[i-5]

for _ in range(int(input())):
    print(pn[int(input())])
    