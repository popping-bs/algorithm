#얼음의 개수

n, m = map(int, input().split())

graph = []

#2차원 리스트의 맵 정보
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >= n  or y <= -1 or y>= m:
        return False
    
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        #여기서 return은 재귀 호출 함수에선 적용 안됨. 오로치 첫 def에서만.
        return True
    return False


#모든 노드(위치)에 대하여 음료수 채우기.
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)