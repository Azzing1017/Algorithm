from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    cur_time = 1
    que = deque([])
    que.append([truck_weights.popleft(), cur_time + bridge_length])
    run_count = 1
    cur_weight = que[0][0]
    
    while truck_weights:
        cur_time += 1
        if que and que[0][1] == cur_time:
            x = que.popleft()
            run_count -= 1
            cur_weight -= x[0]
        if run_count + 1 > bridge_length:
            continue
        elif cur_weight + truck_weights[0] > weight:
            continue
        else:
            y = truck_weights.popleft()
            que.append([y, cur_time + bridge_length])
            run_count += 1
            cur_weight += y
    
    answer = que[-1][1]
        
    return answer