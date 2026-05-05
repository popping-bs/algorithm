from collections import deque
N = int(input())            # 격자 크기
MAP = []                    # 쥐의 위치 정보 지도
R = C = -1                  # 고양이의 위치
LEVEL = 2                   # 고양이의 레벨
EXP = 0                     # 현재 레벨에서 잡은 쥐의 수

ans = 0                     # 고양이가 사냥을 멈출 때까지 걸린 시간

for r in range(N):
    data = list(map(int, input().split()))
    for c in range(N):
        if data[c] == 9:        # 고양이의 위치 찾기 
            R, C = r, c
            data[c] = 0
    MAP.append(data)

def hunt_mouse():
    global R, C, ans
    # 가장 가까운 쥐를 찾고 사냥하기
    q = deque([[R, C, 0]])            # [row, col, time]
    visited = [[False] * N for _ in range(N)]       # 방문 여부 확인 배열
    visited[R][C] = True
    
    best_r = best_c = N + 1         # 가장 가까운 쥐의 위치
    min_time = 1e10                 # 가장 가까운 쥐까지의 거리 (시간)
    while q:
        r, c, time = q.popleft()
        
        ntime = time + 1
        for [dr, dc] in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if visited[nr][nc] or MAP[nr][nc] > LEVEL: continue
            visited[nr][nc] = True
            
            # 가장 가까운 쥐를 찾은 경우 더 먼거리의 쥐는 확인할 필요가 없음
            if min_time < ntime: break
            
            # 사냥 가능한 쥐를 찾은 경우
            if 0 < MAP[nr][nc] < LEVEL:
                # 발견한 쥐들 중 가장 가까운 거리의 쥐인지 확인
                if ntime <= min_time:
                    min_time = ntime
                    # 발견한 쥐는 행이 작은 순, 열이 작은순으로 사냥 함
                    if (best_r, best_c) > (nr, nc):
                        best_r, best_c = nr, nc
            q.append([nr, nc, ntime])
    
    # 가장 가까운 쥐를 찾은 경우
    if (best_r, best_c) != (N + 1, N + 1):
        R, C, MAP[best_r][best_c] = best_r, best_c, 0
        ans += min_time
        return True
    
    return False        # 사냥에 실패 한 경우            
    
def level_up():
    global LEVEL, EXP
    # 경험치를 얻고 레벨업이 가능하면 레벨업 진행
    EXP += 1
    if LEVEL <= EXP: EXP, LEVEL = 0, LEVEL + 1

while True:
    # 가장 가까운 쥐를 찾고 사냥
    if not hunt_mouse(): break
    
    # 사냥한 쥐를 포함한 레벨업 여부 확인
    level_up()

print(ans)