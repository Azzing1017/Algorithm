import sys

li_fibomemo = [0, 1]
def fibo(n):
    global li_fibomemo
    if len(li_fibomemo) > n:
        return li_fibomemo[n]
    else:
        li_fibomemo.append(fibo(n-1) + fibo(n-2))
        return fibo(n-1) + fibo(n-2)
    
fibo(40)

T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    if num == 0:
        sys.stdout.write(f'1 0'+'\n')
    else:
        sys.stdout.write(f'{li_fibomemo[num-1]} {li_fibomemo[num]}'+'\n')