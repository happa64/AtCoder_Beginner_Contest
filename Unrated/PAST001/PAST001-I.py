# https://atcoder.jp/contests/past201912-open/tasks/past201912_i
# I - 部品調達
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    SC = []
    for i in range(m):
        s, c = map(str, input().split())
        s = s.replace('Y', '1').replace('N', '0')
        SC.append([int(s, 2), int(c)])

    # bitDP
    dp = [f_inf for _ in range(1 << n)]
    dp[0] = 0
    for i in range(1 << n):
        for s, c in SC:
            idx = i | s
            dp[idx] = min(dp[idx], dp[i] + c)

    if dp[-1] == f_inf:
        print(-1)
    else:
        print(dp[-1])


if __name__ == '__main__':
    resolve()
