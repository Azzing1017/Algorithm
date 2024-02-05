while True:
    li = list(input())
    if li[0] == '.':
        break
    li_check = []
    tf = True
    for val in li:
        if val == '[':
            li_check.append(val)
        elif val == '(':
            li_check.append(val)
        elif val == ']':
            if not li_check:
                tf = False
                break
            elif li_check.pop() == '[':
                continue
            else:
                tf = False
                break
        elif val == ')':
            if not li_check:
                tf = False
                break
            elif li_check.pop() == '(':
                continue
            else:
                tf = False
                break
        else:
            continue
    if tf and not li_check:
        print('yes')
    else:
        print('no')