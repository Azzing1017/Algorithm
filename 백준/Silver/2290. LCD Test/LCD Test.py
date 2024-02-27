import sys

s, n = map(int, sys.stdin.readline().split())
li = list(str(n))

arr1 = [[' ']*(s+3) for _ in range(2*s+3)]
arr2 = [[' ']*(s+3) for _ in range(2*s+3)]
arr3 = [[' ']*(s+3) for _ in range(2*s+3)]
arr4 = [[' ']*(s+3) for _ in range(2*s+3)]
arr5 = [[' ']*(s+3) for _ in range(2*s+3)]
arr6 = [[' ']*(s+3) for _ in range(2*s+3)]
arr7 = [[' ']*(s+3) for _ in range(2*s+3)]
arr8 = [[' ']*(s+3) for _ in range(2*s+3)]
arr9 = [[' ']*(s+3) for _ in range(2*s+3)]
arr0 = [[' ']*(s+3) for _ in range(2*s+3)]
# 1
for i in range(1, s+1):
    arr1[i][s +1] = '|'
for i in range(s+2, 2*s+2):
    arr1[i][s +1] = '|'
# 2
for i in range(1, s+1):
    arr2[0][i] = '-'
for i in range(1, s+1):
    arr2[i][s +1] = '|'
for i in range(1, s+1):
    arr2[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr2[i][0] = '|'
for i in range(1, s+1):
    arr2[2*s +2][i] = '-'
# 3
for i in range(1, s+1):
    arr3[0][i] = '-'
for i in range(1, s+1):
    arr3[i][s +1] = '|'
for i in range(1, s+1):
    arr3[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr3[i][s +1] = '|'
for i in range(1, s+1):
    arr3[2*s +2][i] = '-'
# 4
for i in range(1, s+1):
    arr4[i][0] = '|'
    arr4[i][s +1] = '|'
for i in range(1, s+1):
    arr4[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr4[i][s +1] = '|'
# 5
for i in range(1, s+1):
    arr5[0][i] = '-'
for i in range(1, s+1):
    arr5[i][0] = '|'
for i in range(1, s+1):
    arr5[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr5[i][s +1] = '|'
for i in range(1, s+1):
    arr5[2*s +2][i] = '-'
# 6
for i in range(1, s+1):
    arr6[0][i] = '-'
for i in range(1, s+1):
    arr6[i][0] = '|'
for i in range(1, s+1):
    arr6[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr6[i][0] = '|'
    arr6[i][s +1] = '|'
for i in range(1, s+1):
    arr6[2*s +2][i] = '-'
# 7
for i in range(1, s+1):
    arr7[0][i] = '-'
for i in range(1, s+1):
    arr7[i][s +1] = '|'
for i in range(s+2, 2*s+2):
    arr7[i][s +1] = '|'
# 8
for i in range(1, s+1):
    arr8[0][i] = '-'
for i in range(1, s+1):
    arr8[i][0] = '|'
    arr8[i][s + 1] = '|'
for i in range(1, s+1):
    arr8[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr8[i][0] = '|'
    arr8[i][s +1] = '|'
for i in range(1, s+1):
    arr8[2*s +2][i] = '-'
# 9
for i in range(1, s+1):
    arr9[0][i] = '-'
for i in range(1, s+1):
    arr9[i][0] = '|'
    arr9[i][s + 1] = '|'
for i in range(1, s+1):
    arr9[s +1][i] = '-'
for i in range(s+2, 2*s+2):
    arr9[i][s +1] = '|'
for i in range(1, s+1):
    arr9[2*s +2][i] = '-'
# 0
for i in range(1, s+1):
    arr0[0][i] = '-'
for i in range(1, s+1):
    arr0[i][0] = '|'
    arr0[i][s + 1] = '|'
for i in range(s+2, 2*s+2):
    arr0[i][0] = '|'
    arr0[i][s +1] = '|'
for i in range(1, s+1):
    arr0[2*s +2][i] = '-'

ans = []
for x in li:
    if x == '1':
        ans.append(arr1)
    elif x == '2':
        ans.append(arr2)
    elif x == '3':
        ans.append(arr3)
    elif x == '4':
        ans.append(arr4)
    elif x == '5':
        ans.append(arr5)
    elif x == '6':
        ans.append(arr6)
    elif x == '7':
        ans.append(arr7)
    elif x == '8':
        ans.append(arr8)
    elif x == '9':
        ans.append(arr9)
    elif x == '0':
        ans.append(arr0)

answer = []
for n in range(2*s+3):
    tmp = ''
    for var in ans:
        tmp += ''.join(map(str, var[n]))
    answer.append(tmp)

sys.stdout.write('\n'.join(map(str, answer)))
