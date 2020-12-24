# https://atcoder.jp/contests/joi2011ho/submissions/18970244
# B - 古本屋 (Books)
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    CG = [[] for _ in range(10)]
    for _ in range(n):
        c, g = map(int, input().split())
        CG[g - 1].append(c)

    book = []
    for i in range(10):
        if CG[i]:
            CG[i].sort(reverse=True)
            CG[i] = [a + idx * (idx + 1) for idx, a in enumerate(accumulate(CG[i]))]
            book.append(CG[i])

    m = len(book)
    dp = [[-f_inf] * (k + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0
    for i in range(1, m + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
        for l, b in enumerate(book[i - 1], 1):
            for j in range(k + 1):
                if j - l < 0:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + b)
    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
