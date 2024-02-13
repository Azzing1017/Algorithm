arr = input().strip()

num = ''
li_num = []
li_a = []
for i in arr:
    if i.isdecimal():
        num += i
    else:
        li_num.append(int(num))
        li_a.append(i)
        num = ''
li_num.append(int(num))

ans = li_num[0]
temp = 0
li_num = li_num[1:]
for i in range(len(li_a)):
    if temp != 0:
        if li_a[i] == '+':
            temp += li_num[i]
        elif li_a[i] == '-':
            ans -= temp
            temp = li_num[i]
    elif temp == 0:
        if li_a[i] == '+':
            ans += li_num[i]
        elif li_a[i] == '-':
            temp = li_num[i]
if temp != 0:
    ans -= temp

print(ans)