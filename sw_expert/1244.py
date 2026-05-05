import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline



def solve(num_str, chg):
    
    n_array = list(num_str)
    chg_int = int(chg)
    
    n_array_length = len(n_array)
    visited = set()
    best = 0

    def dfs(depth):
        nonlocal best

        s = ''.join(n_array)

        if (s,depth) in visited:
            return
        visited.add((s,depth))

        if depth == chg_int:
            best = max(best, int(s))
            return

        for i in range(n_array_length-1):
            for j in range(i+1, n_array_length):
                n_array[i] , n_array[j] = n_array[j], n_array[i]
                dfs(depth+1)
                n_array[i] , n_array[j] = n_array[j], n_array[i]
    dfs(0)

    return best

T = int(input())

for tc in range(1, T+1):
    num_str, chg = input().split()

    print(f"#{tc} {solve(num_str, chg)}")