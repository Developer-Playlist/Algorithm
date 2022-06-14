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


















###
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 입력예시
# # key
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# # lock
# [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 출력예시
# true

# 모범답안
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
###
