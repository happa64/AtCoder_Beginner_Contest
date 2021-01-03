# https://atcoder.jp/contests/abc187/submissions/19176210
# F - Close Group
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    E = [0] * n
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        E[a] |= 1 << b
        E[b] |= 1 << a

    dp = [f_inf] * (1 << n)
    dp[0] = 1
    for S in range(1 << n):
        for v in range(n):
            if dp[S] == 1 and not (S & (1 << v)) and S & E[v] == S:
                dp[S | (1 << v)] = 1

        s = (S - 1) & S
        while s > 0:
            dp[S] = min(dp[S], dp[s] + dp[S ^ s])
            s = (s - 1) & S

    print(dp[-1])


if __name__ == '__main__':
    resolve()
