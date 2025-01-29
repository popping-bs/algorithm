# n, m 공백으로 입력
n, m = map(int, input().split())
# 캐릭터 현재 위치, 바라보는 방향 입력.
x, y, direction = map(int, input().split())

#방문 기록 유무 확인
d = [ [0]*m for _ in range(n) ]
d[x][y] = 1

#전체 맵 정보를 입력 받기.
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] ==0 and array[nx][ny] ==0:
        d[nx][ny] =1
        x = nx
        y = ny
        count += 1
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)