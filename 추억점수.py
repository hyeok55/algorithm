def solution(name, yearning, photo):
    answer = []
    result = {}
    for i in range(len(name)):
        result[name[i]] = yearning[i]
    score = 0
    for people in photo:
        for human in people:
            if human in name:
                score += result[human]
        answer.append(score)
        score = 0