import sys
import math

N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
count = n_list[-1]
pn_list = [0]*(count+1)
max = int(math.sqrt(count))
pn_list[1] = 1

for i in range(2, max+1):
    if pn_list[i] == 0:
        per = 2
        while i*per<=count:
            pn_list[i*per] = 1
            per += 1

prime_count = 0
for k in n_list:
    if pn_list[k] == 0:
        prime_count += 1

sys.stdout.write(str(prime_count))