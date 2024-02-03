while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    li.sort()
    if li[2]**2 == li[1]**2 + li[0]**2:
        print('right')
    else:
        print('wrong')