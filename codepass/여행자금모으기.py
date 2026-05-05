import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline


N = int(input())
print('N',N)
ARR = []
for _ in range(N):
    T, P = map(int,input().split())
    ARR.append((T,P))

ans = 0
def work(day, income):
    global ans
    # 종료 조건 1
    if day > N: return
    if day == N:
        ans = max(ans, income)
        return

    #현재 day날에 작업 하지 않는경우
    work(day +1, income)
    work(day + ARR[day][0], income + ARR[day][1])

work(0,0)

print(ans)