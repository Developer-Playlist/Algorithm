###
# <현지> [O]
def solution(s):
    result=[]
    if len(s) == 1:
        return 1
    for i in range(1, len(s)+1):
        b = ''
        count = 1
        word=s[:i]

        for j in range(i, len(s)+i, i):
            if word==s[j:i+j]:
                count+=1
            else:
                if count!=1:
                    b = b + str(count)+word #글자만들기
                else:
                    b = b + tmp
                    
                word=s[j:j+i]
                count = 1
        result.append(len(b))
    return min(result)
###

###
# <기성> []
###


















###
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 입력예시
# "aabbaccc"

# 출력예시
# 7

# 모범답안
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 +1):
        compressed = ""
        prev =s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[s:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
            compressed += str(count) + prev if count >= 2 else prev
            answer = min(answer, len(compressed))
        return answer
###
