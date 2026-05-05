N, L, R = map(int, input().split())                         # 격자 크기, 바나나 차이 (최솟값, 최댓값)
MAP = [list(map(int, input().split())) for _ in range(N)]   # 바나나 개수 2차원 배열

ans = 0                                 # 재분배 횟수
visit = [[-1] * N for _ in range(N)]    # 그룹 생성 시 방문 여부 저장
check = [[-1] * N for _ in range(N)]    # 재분배 시 방문 여부 저장

def make_group(r, c):
    visit[r][c] = ans                   # 방문 체크
    cnt, sum_ba = 1, MAP[r][c]          # 그룹 우리의 수, 바나나 총수 초기화
    for [dr, dc] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        # 격자 테두리 확인 및 방문 여부 확인
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if visit[nr][nc] == ans: continue
        # 철창 open 여부 확인
        if L <= abs(MAP[r][c] - MAP[nr][nc]) <= R:
            _cnt, _sum_ba = make_group(nr, nc)      # 그룹 우리의 수, 바나나 총수
            cnt += _cnt
            sum_ba += _sum_ba
    return cnt, sum_ba
 
def redistribute(r, c, value):
    check[r][c] = ans                   # 방문 체크
    for [dr, dc] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        # 격자 테두리 확인 및 방문 여부 확인
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if check[nr][nc] == ans: continue
        # 철창 open 여부 확인
        if L <= abs(MAP[r][c] - MAP[nr][nc]) <= R:
            redistribute(nr, nc, value)
    MAP[r][c] = value                               # 바나나 재분배 적용
 
def redistribute_all():
    is_chagned = False          # 재분배 수행 여부
    for r in range(N):
        for c in range(N):
            # 이미 재분배가 되었는지 확인
            if visit[r][c] == ans: continue
            cnt, sum_ba = make_group(r, c)       # 재분배 그룹의 우리 수, 바나나 총합 

            if cnt == 1: continue               # 1칸인 경우 재분배 수행하지 않음
            
            # 재분배 수행
            is_chagned = True
            redistribute(r, c, sum_ba // cnt)   # 바나나 재분부
            
    return is_chagned
            
while True:
    # 바나나 재분배 수행
    if not redistribute_all(): break    # 재분배 수행 여부 확인
    ans += 1

print(ans)