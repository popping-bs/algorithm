import sys

'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
'''

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N , S = map(int, input().split())
nums = list(map(int, input().split()))

s = 0
left = 0
ans = N + 1


for right in range(N):
    s += nums[right]

    while s >= S:
        ans = min(ans, right - left + 1)
        s -= nums[left]
        left += 1


print(0 if ans == N+1 else ans)