# https://atcoder.jp/contests/joi2014ho/submissions/18961558
# B - IOI饅頭（IOI Manju）
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    m, n = map(int, input().split())
    P = [int(input()) for _ in range(m)]
    BOX = [list(map(int, input().split())) for _ in range(n)]
    P.sort(reverse=True)
    A = [0] + list(accumulate(P))

    dp = [[f_inf] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        c, e = BOX[i - 1]
        for j in range(m + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j - c < 0:
                dp[i][j] = min(dp[i][j], e)
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - c] + e)
    B = [0] + dp[-1]

    res = 0
    for a, b in zip(A, B):
        res = max(res, a - b)
    print(res)


if __name__ == '__main__':
    resolve()
