import sys
from collections import defaultdict


sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N,M,K = map(int,input().split())
MAP = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    row,col,weight, speed,direction = map(int,input().split())
    MAP[row -1][col -1].append([weight,speed,direction])

DIR = [[-1, 0], [-1, 1], [0, 1], [1, 1], 
       [1, 0], [1, -1], [0, -1], [-1, -1]]
def move_all():
    new_map = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for [w,s,d] in MAP[r][c]:
                nr = (r + DIR[d][0] * s) % N
                nc = (c + DIR[d][1] * s) % N
                new_map[nr][nc].append([w,s,d])
    return new_map

def comp_and_decomp():
    new_map = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if len(MAP[r][c]) <2:
                new_map[r][c] = MAP[r][c]
                continue

            total_weight = total_speed = 0

            for [w,s,_] in MAP[r][c]:
                total_weight += w
                total_speed += s

            first_dir = MAP[r][c][0][2] % 2 
            is_cross_dir = 0
            for *_ , d in MAP[r][c]:
                if d % 2 != first_dir:
                    is_cross_dir = 1
                    break

            new_weight = total_weight // 5
            new_speed = total_speed // len(MAP[r][c])

            if new_weight ==0: continue

            for i in range(4):
                new_map[r][c].append([new_weight,new_speed, 2*i + is_cross_dir])

    return new_map

for _ in range(K):
    MAP = move_all()

    MAP = comp_and_decomp()


print(sum([
    w
    for r in range(N)
    for c in range(N)
    for w, *_ in MAP[r][c]]))