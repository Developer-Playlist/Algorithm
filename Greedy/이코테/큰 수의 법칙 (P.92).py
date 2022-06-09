###
# <지수> [X]

# 생각했던 로직
#일단 N을 가장 큰수부터 정렬 후, 가장 큰 수를 K번만큼 반복하는데 총 M번 만큼 반복

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬 
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 가장 큰 수 

result = 0

while True:
  for i in range(k):
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first # 가장 큰 수 한 번 더하기
    m -= 1 # 더할 때마다 m에서 1씩 빼기
  if m == 0:
    break
  result += second # 두 번째로 가장 큰 수 한 번 더하기
  m -= 1 # 더할 때마다 m에서 1씩 빼기 
  
print(result)


###

