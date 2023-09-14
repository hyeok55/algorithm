def solution(park, routes):
    # 세로 n , 가로 m  좌표는 (n,m)
    
    n,m = len(park), len(park[0])
    plans = ["E","W","S","N"]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    
    #현재 위치 파악

    for r in range(n):
        for b in range(m):
            if park[r][b] == "S":
                sx,sy = r,b
    
    
    for route in routes:
        direction, length = route[0], int(route[2:])
        
        ignore = False
    #route를 일단 방향과 길이로 쪼개서 받고
        # 예상 좌표
        ex,ey = sx,sy
        for j in range(4):
            
            #방향 확인 조건
            if direction == plans[j]:
                
                #길이 만큼 명령 반복
                for i in range(length):
                    
                    ex += dx[j]
                    ey += dy[j]
                    # 이동
                    if ex < 0 or ex > n-1 or ey < 0 or ey > m-1:
                        ignore = True
                        break
                    # 조건 1 = 지나가는 라인에 x가 없는가
                    if park[ex][ey] == "X":
                        ignore = True
                        
                    # 조건 2 = 명령을 다 완료 했을 시에 외곽 여부
                if ex < 0 or ex > n-1 or ey < 0 or ey > m-1:
                    ignore = True
            
        if ignore == False:
            sx, sy = ex,ey
    

    return [sx,sy]
