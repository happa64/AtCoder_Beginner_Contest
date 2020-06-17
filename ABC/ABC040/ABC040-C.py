# https://atcoder.jp/contests/abc040/submissions/14432862
# C - 柱柱柱柱柱
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [f_inf] * n
    dp[0] = 0
    dp[1] = abs(A[1] - A[0])
    for i in range(2, n):
        dp[i] = min(dp[i], dp[i - 1] + abs(A[i] - A[i - 1]), dp[i - 2] + abs(A[i] - A[i - 2]))

    print(dp[-1])


if __name__ == '__main__':
    resolve()
