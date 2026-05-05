import sys


#투포인터 알고리즘
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
s = 0
left = 0


for right in range(N):
    s += nums[right]

    while s > M:
        s -= nums[left]
        left += 1

    if s == M:
        count += 1

print(count)