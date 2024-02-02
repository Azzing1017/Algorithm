while True:
    num = list(input())
    if num[0] == '0':
        break
    check = 'yes'
    for i in range(len(num)//2+1):
        if num[i] != num[-i-1]:
            check = 'no'
            break
    print(check)       