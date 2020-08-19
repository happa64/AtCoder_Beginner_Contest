# https://atcoder.jp/contests/joi2007yo/submissions/16034878
# F - 通学経路
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B = map(int, input().split())
    n = int(input())
    XY = set(tuple(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)))

    dp = [[0] * B for _ in range(A)]
    dp[0][0] = 1
    for a in range(A):
        for b in range(B):
            if (a, b) in XY:
                continue
            if a - 1 >= 0:
                dp[a][b] += dp[a - 1][b]
            if b - 1 >= 0:
                dp[a][b] += dp[a][b - 1]
    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
