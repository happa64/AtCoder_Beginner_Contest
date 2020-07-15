# https://atcoder.jp/contests/abc041/submissions/15238461
# D - 徒競走
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    YX = set(tuple(tuple(map(lambda x: int(x) - 1, input().split()))[::-1]) for _ in range(m))

    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1 << n):
        for nxt in range(n):
            if not (S & (1 << nxt)):
                flg = True
                for prev in range(n):
                    if S & (1 << prev):
                        if (prev, nxt) in YX:
                            flg = False
                if flg:
                    dp[S | (1 << nxt)] += dp[S]
    print(dp[-1])


if __name__ == '__main__':
    resolve()
