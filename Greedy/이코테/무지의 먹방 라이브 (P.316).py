###
# <기성> [X] : ㅋㅋ,, 하,,
def solution(food_times, k):
    iter = sum(food_times)
    length =  len(food_times)
    limit =0
    if iter >= k:
        for i in range(iter):
            if i != 0:
                loop = length // i
                if loop == length:
                    limit += 1
            loop_idx = i - length * (limit - 1)
            if food_times[loop_idx] == 0:
                pass
            else:
                food_times[loop_idx] -= 1
        answer = loop_idx + 1
    else:
        answer = -1

    return answer

print(solution([3, 1, 2], 5))

# <기성 2> [X] : 2/100 -> 런타임 에러 -> 그리디로 풀어야함
def solution(food_times, k):
    iter = sum(food_times)
    length = len(food_times)
    zero_count = 0
    limit = 0
    if iter >= k:
        for i in range(k+1):
            if i >= length:
                loop = length // i
                if loop == 1:
                    limit += 1
            loop_idx = i - length * limit
            if food_times[loop_idx] == 0:
                zero_count += 1
                pass
            else:
                food_times[loop_idx] -= 1
        answer = loop_idx + zero_count + 1 - length * limit
    else:
        answer = -1

    return answer
###

# <현지> [X] : 어디서부터 잘못된지 모르겠어서 답지 봄..
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1 
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i))
    used = 0
    previous = 0
    remain = len(food_times)
    while (used + ((q[0][0] - previous) * remain) <= k):
        now = heapq.heappop(q)[0]
        used = used + (now - previous) * remain
        remain = remain - 1
        previous = now
    answer = sorted(q, key=lambda x: x[1])
    return answer[(k - used) % remain][1]
###


