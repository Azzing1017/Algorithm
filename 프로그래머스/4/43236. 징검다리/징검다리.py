def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = [0] + rocks + [distance]
    l = len(rocks)
    s, e = 0, distance
    while s <= e:
        m = (s + e) // 2

        cnt = 0
        st = 0
        tf = [True] * l

        for i in range(1, l):
            d = rocks[i] - rocks[st]
            if d < m:
                if rocks[i] == distance:
                    tf[st] = False
                    cnt += 1
                    nn = 1
                    while (st - nn) >= 0:
                        if tf[st - nn]:
                            d = rocks[i] - rocks[st - nn]
                            if d < m:
                                tf[st - nn] = False
                                cnt += 1
                            else:
                                break
                        nn += 1

                else:
                    tf[i] = False
                    cnt += 1
            else:
                st = i
        if cnt > n:
            e = m - 1
        elif cnt <= n:
            answer = m
            s = m + 1

    return answer
            