###
# 기성 [X] : ㅋㅋ,, 하,,
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
###
