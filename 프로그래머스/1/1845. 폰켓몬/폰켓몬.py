def solution(nums):
    answer = 0
    uli = set(nums)
    lena = len(nums)//2
    lenb = len(uli)
    if lena > lenb:
        answer = lenb
    else:
        answer = lena
        
    return answer