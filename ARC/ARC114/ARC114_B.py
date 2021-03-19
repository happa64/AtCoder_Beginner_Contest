# https://atcoder.jp/contests/arc114/submissions/21033242
# B - Special Subsets
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 998244353


def solve():
    n = int(input())
    F = list(map(lambda x: int(x) - 1, input().split()))

    cycle_cnt = 0
    visited = [False] * n
    for i, f in enumerate(F):
        if visited[i]:
            continue
        check = set()
        now = i
        flg = True
        while True:
            if now in check:
                break
            if visited[now]:
                flg = False
                break
            visited[now] = True
            check.add(now)
            now = F[now]
        if flg:
            cycle_cnt += 1

    res = pow(2, cycle_cnt, MOD) - 1
    print(res % MOD)


if __name__ == '__main__':
    solve()
