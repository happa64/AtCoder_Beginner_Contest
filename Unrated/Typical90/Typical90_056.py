# https://atcoder.jp/contests/typical90/submissions/23150182
# 056 - Lucky Bag（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, s = map(int, input().split())
    AB = tuple(tuple(map(int, input().split())) for _ in range(n))

    dp = [[-1] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        a, b = AB[i]
        for j in range(s + 1):
            if dp[i][j] == -1:
                continue
            if j + a <= s:
                dp[i + 1][j + a] = 1
            if j + b <= s:
                dp[i + 1][j + b] = 2

    if dp[-1][-1] == -1:
        print("Impossible")
        exit()

    res = ""
    now = s
    for i in reversed(range(n)):
        a, b = AB[i]
        if now - a >= 0 and dp[i][now - a] != -1:
            res += "A"
            now -= a
        elif now - b >= 0 and dp[i][now - b] != -1:
            res += "B"
            now -= b
    print(res[::-1])


if __name__ == '__main__':
    solve()
