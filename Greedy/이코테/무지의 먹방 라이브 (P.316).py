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
