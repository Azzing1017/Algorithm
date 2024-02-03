N = int(input())
li_N = list(map(int, input().split()))
M = int(input())
li_M = list(map(int, input().split()))
li_N.sort()

def go(start, end, num):
    global li_N
    if li_N[start] == num:
        print(1)
        return
    elif li_N[end] == num:
        print(1)
        return
    elif end - start == 1:
        print(0)
        return
    a = (start+end)//2
    if li_N[a] > num:
        return go(start, (start+end+1)//2, num)
    elif li_N[a] < num:
        return go(a, end, num)
    elif li_N[a] == num:
        print(1)
        return
    
end = len(li_N)-1
for i in li_M:
    go(0, end, i)