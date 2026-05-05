import copy
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 데이터 입력 받기
N = 4                                                   # 격자 크기
EMPTY = [0, 0]                                          # 빈 칸
MAP = [[EMPTY for _ in range(N)] for _ in range(N)]     # 파리의 정보(파리의 수, 방향) 지도

for r in range(N):
    data = list(map(int, input().split()))
    for c in range(0, 2 * N, 2):
        MAP[r][c // 2] = [data[c], data[c + 1] - 1]

# 8방향(북쪽 부터 45도씩 반시계 방향, 0 ~ 7)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0                             # 잡아 먹은 파리의 최댓값
FR = FC = 0                         # 개구리의 위치

def next_fly_pos(r, c, d):
    # 이동 가능한 방향을 살펴보기
    for i in range(8):
        nd = (d + i) % 8
        nr, nc = r + dr[nd], c + dc[nd]
        
        # 범위 내인지, 개구리가 있는지 확인
        if (0 <= nr < N and 0 <= nc < N) and (nr, nc) != (FR, FC):
            return nr, nc ,nd
    return r, c, d 

def move_fly(num):
    # 모든 칸에 대해서 num에 해당하는 파리그룹의 움직임 수행
    for r in range(N):
        for c in range(N):
            if MAP[r][c][0] != num: continue
            # 파리가 새로 움직일 칸
            nr, nc, nd = next_fly_pos(r, c, MAP[r][c][1])

            # 파리의 위치를 서로 교환
            if (nr, nc) != (r, c):
                MAP[r][c], MAP[nr][nc] = MAP[nr][nc], [num, nd]
                return 

def fly_hunting(r, c, score):
    global ans, FR, FC, MAP
    # 종료조건
    if MAP[r][c] == EMPTY: return
    
    prev_map = copy.deepcopy(MAP)   # 현재 지도 저장 
    
    # 현재 위치의 파리를 사냥
    score += MAP[r][c][0]           # 잡아 먹은 파리의 수만큼 점수 획득
    dir = MAP[r][c][1]              # 잡아 먹은 파리의 방향이 개구리의 방향
    FR, FC = r, c                   # 개구리의 위치 업데이트
    MAP[r][c] = EMPTY               # 빈칸으로 만들기
    
    ans = max(ans, score)           # 잡아 먹은 파리의 수의 최댓값    

    # 파리의 이동
    for i in range(1, 17): move_fly(i)

    # 개구리가 점프 할 수 있는 곳을 살펴보기
    while True:
        r, c = r + dr[dir], c + dc[dir]
        
        # 개구리가 갈 수 있는 곳인지 확인
        if r < 0 or r >= N or c < 0 or c >= N: break
        fly_hunting(r, c, score)
    
    MAP = copy.deepcopy(prev_map)

fly_hunting(0, 0, 0)
print(ans)