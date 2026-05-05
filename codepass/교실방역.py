import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N,M = map(int, input().split())
MAP = []
MACHINE_LIST = []

ans = 10 ** 18
machine_rotated_list = []

disinfected_dir = [  
    [],
    [0,1,0,0],
    [0,1,0,1],
    [1,1,0,0],
    [1,1,0,1],
    [1,1,1,1]
]

machine_can_rotate = [0,4,2,4,4,1]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for r in range(N):
    data = list(map(int,input().split()))
    for c in range(M):
        if 1<= data[c] <=5: MACHINE_LIST.append([r,c,data[c]])
    MAP.append(data)

def get_area():
    disinfected = [[False]*M for _ in range(N)]
    for [row,col,rot,t] in machine_rotated_list:
        disinfected[row][col] = True
        for d in range(4):
            if disinfected_dir[t][(d-rot)%4]:
                nr,nc = row, col
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    if nr< 0 or nr >= N or nc <0 or nc>=M: break
                    if MAP[nr][nc] ==6: break 
                    disinfected[nr][nc] = True

    area = sum([
        1
        for r in range(N)
        for c in range(M)
        if not disinfected[r][c] and MAP[r][c] !=6
    ])
    return area


def get_min_area(m_idx):
    global ans

    if m_idx == len(MACHINE_LIST):
        ans = min(ans,get_area())
        return
    
    row, col, t = MACHINE_LIST[m_idx]

    for rot in range(machine_can_rotate[t]):
        machine_rotated_list.append([row,col,rot,t])
        get_min_area(m_idx + 1)
        machine_rotated_list.pop()


get_min_area(0)
print(ans)

