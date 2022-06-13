###
#<지수>[X]
#int로만 생각했다... 좌표 x, y로 로직 생각을 못해따....

n = int(input())
k = list(map(input().split()))

start = [1,1]

for i in start:
    if i=='L':
        if start[1]>1:
            start[1]-=1
    elif i=='R':
        if start[1]<1:
            start[1]+=1
    elif i=='U':
        if start[0]>1:
            start[0]-=1
    elif i=='D':
        if now[1]<1:
            now[0]+=1

print(start)

###

###
#정답
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans: #이동 계획 확인
    for i in range(len(move_types)): #이동 후 좌표
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n: #공간 벗어나면 무시하기
        continue
        
    x, y = nx, ny #이동 수행 

print(x, y)

###
