def solution(cards1, cards2, goal):
    
    ans_one = []
    ans_two = []

        
    
    for word in goal:
        if word in cards1:
            ans_one.append(word)
            
        if word in cards2:
            ans_two.append(word)
    
    a = len(ans_one)
    b = len(ans_two)
    # 카드뭉치의 단어를 다 쓸 필요가 없음
    if ans_one == cards1[:a] and ans_two == cards2[:b]:
        return "Yes"
    else:
        return "No"