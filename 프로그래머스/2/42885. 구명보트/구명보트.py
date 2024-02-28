def solution(people, limit):
    answer = 0
    people.sort()
    l = len(people)
    cnt = 0
    left, right = 0, l-1
    while left < right:
        if people[left] + people[right] <= limit:
            cnt += 1
            left += 1
            right -= 1
        else:
            right -= 1
    answer = l-cnt
    return answer