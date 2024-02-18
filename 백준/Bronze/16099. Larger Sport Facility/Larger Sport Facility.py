for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    lwt = lt * wt
    lwe = le * we
    if lwt > lwe:
        print('TelecomParisTech')
    elif lwt < lwe:
        print('Eurecom')
    elif lwt == lwe:
        print('Tie')
