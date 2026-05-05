import sys

sys.stdin = open('input.txt','r')
N, S = map(int, input().split())
rcv_nums = list(map(int, input().split()))
visited = [False] * N
#크기가 양수인 부분수열? => len이 0보다 큰 ? 무조건 1개이상의 원소?

nums = []
count = 0

def dfs2(start):
    global count

    for i in range(start, N):
        nums.append(rcv_nums[i])
        if sum(nums) == S:
            count+=1

        dfs2(i+1)
        nums.pop()

dfs2(0)
print(count)
