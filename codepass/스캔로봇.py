import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
SCAN_MAP = [[False]* M for _ in range(N)]


dir = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 0

def rotate_robot():
    for i in range(1,5):
        nd = (d-i) % 4
        nr,nc = r + dir[nd][0], c + dir[nd][1]

        if MAP[nr][nc] ==1 or SCAN_MAP[nr][nc]: continue
        
        return nr,nc,nd
    
    return r,c,d

def moving_robot():
    global ans, r,c,d
    if not SCAN_MAP[r][c]: ans +=1
    SCAN_MAP[r][c] = True

    nr,nc,nd = rotate_robot()

    if (nr,nc) == (r,c):
        nr,nc = r - dir[d][0], c -dir[d][1]
        if MAP[nr][nc] ==1: return False

    r,c,d = nr,nc,nd
    return True


while True:
    if not moving_robot(): break


print(ans)