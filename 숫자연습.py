def solution(X, Y):
    answer = ""
    # 한번에 정렬까지 가능함 지린다..
    for i in range(9,-1,-1):
        answer += (str(i)* min(X.count(str(i)), Y.count(str(i))))
    
    if answer == "":
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer