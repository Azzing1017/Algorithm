list_input = list(map(int, input().split()))

def music_check(index):
    global list_input
    num1 = list_input[index]
    num2 = list_input[index+1]
    if num1 < num2:
        return 'ascending'
    elif num1 > num2:
        return 'descending'

check_now = music_check(0)
for i in range(1, len(list_input)-1):
    if music_check(i) == check_now:
        continue
    else:
        check_now = 'mixed'
        break

print(check_now)