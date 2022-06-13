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
