###
# <현지> [X] 문제 이해하는데만 30분걸렸습니다..

def solution(key, lock):
    return answer
###


###
# <기성> [] : 
# 완전탐색으로 생각됌
# 2N-2 + M 의 2차원 배열; (N-1 -1, N-1 -1) ~ (N-1 + M -1, N-1 + M -1) 까지 lock을 넣음, 나머진 다 0
# (0,0) 부터 키를 넣고, 글쓰는 방향으로 탐색을 함 (한 위치에서 시계방향 회전도 함 (90, 180, 270, 360))
# lock 부분 <(N-1 -1, N-1 -1) ~ (N-1 + M -1, N-1 + M -1)> 이 모두 1로 채워지면 true 반환

###
