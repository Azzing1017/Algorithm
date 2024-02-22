def solution(phone_book):
    answer = True
    phone_book.sort()
    len_pb = len(phone_book)
    if len_pb == 1:
        answer = False
    else:
        for i in range(len_pb-1):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer