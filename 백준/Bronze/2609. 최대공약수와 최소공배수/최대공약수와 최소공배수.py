import sys

def gcf(m, n):
    if n == 0:
        return m
    else:
        return gcf(n, m%n)

a, b = map(int, input().split())

if min(a, b) == a:
    m = b
    n = a
else:
    m = a
    n = b
    
gc_list = []
gc_list.append(gcf(m, n))
gc_list.append(int(m*n/gc_list[0]))

sys.stdout.write('\n'.join(map(str, gc_list))+'\n')