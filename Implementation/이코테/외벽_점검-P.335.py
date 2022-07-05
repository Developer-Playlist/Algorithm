###

# 1차 생각
# 간격 정렬 [원형이니깐 / 총 길이를 기준으로 간격 재기] ; 우선 이것부터 난관 ; 입력예시: [1, 5, 6, 10]
# -> 리스트를 한번 더 붙히는 아이디어로 접근 (?)

# weak 에서 pop 으로 꺼내면서 (큰 수)
# 간격에 대해 커버한다?

# 2차 생각
# 단순히 weak 위치에 대해 dist 원소가 커버 가능하게?
# 그 커버를 계산하는 로직은 1차 생각때 처럼 리스트를 한번 더 붙힌다

# <기성> [X] : 
def solution(n, weak, dist):
    big = dist.pop()

    x = 1e9
    for p in weak:

    answer = 0
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
solution(n, weak, dist)
###