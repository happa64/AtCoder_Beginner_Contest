# https://atcoder.jp/contests/joi2012ho/submissions/17063338
# B - たのしいカードゲーム (Card Game is Fun)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ab = list(map(int, input().split()))
    if len(ab) == 2:
        a, b = ab
    else:
        a = ab[0]
        b = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [0] * (b + 1)
    for i in range(a):
        next_dp = [0] * (b + 1)
        for j in range(b):
            if A[i] == B[j]:
                next_dp[j + 1] = max(next_dp[j + 1], dp[j] + 1)
            else:
                next_dp[j + 1] = dp[j + 1]
        dp = next_dp
    print(max(dp))


if __name__ == '__main__':
    resolve()
