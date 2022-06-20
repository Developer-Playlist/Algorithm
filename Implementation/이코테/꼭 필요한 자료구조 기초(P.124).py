### 스택, 큐, 재귀 함수 이해하기
#<지수> 
##스택
#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최상단 원소부터 출력
print(stack[::-1]) #최하단 원소부터 출력
#

##큐
#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()

from collections import deque #deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse()
print(queue) #나중에 들어온 순서대로 출력
#

##재귀함수 종료 조건
#재귀 함수를 문제 풀이에서 사용할 때는 종료 조건을 반드시 명시해야함. 아니면 함수가 무한히 호출됨.
def recursive_function(i):
  if i == 100: #100번째 출력했을 때 종료되도록 종료 조건 명시
    return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다. ')
    recursive_function(i + 1) #함수의 매개변수로 i가 들어왔을 때 i + 1로 다음 재귀함수를 호출
    print(i, '번째 재귀 함수를 종료합니다. ')
   
recursive_function(1)
#

##팩토리얼
#반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  for i in range(i, n+1): #1부터 n까지의 수를 차례대로 곱하기
    result *= i 
  return result
  
print('반복적으로 구현:', factorial_iterative(5))
  
#재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: #n이 1이하인 경우 1을 반환. 1!는 1이기 때문
    return 1
  return n * factorial_recursive(n - 1) 
  #n! = n * (n - 1)!를 그대로 코드로 작성, 자기자신 n에 n보다 1작은 팩토리얼 호출한 값을 곱한 결과를 반환. n이 5라면 5*4! 반환됨

print('재귀적으로 구현:', factorial_recursive(5))
#
###
