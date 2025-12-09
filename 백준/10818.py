import sys



sys.stdin = open('input.txt','r')

n = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))


min_n = min(nums)
max_n = max(nums)

print(f"{min_n} {max_n}")