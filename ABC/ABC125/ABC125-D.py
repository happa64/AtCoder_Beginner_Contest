# https://atcoder.jp/contests/abc125/submissions/14484805
# D - Flipping Signs
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    total = 0
    mi = f_inf
    for a in A:
        total += abs(a)
        if a < 0:
            cnt += 1
        if mi > abs(a):
            mi = abs(a)

    if cnt % 2 == 0:
        print(total)
    else:
        print(total - mi * 2)


def resolve2():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    dp[0][1] = -f_inf
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0] + A[i - 1], dp[i - 1][1] - A[i - 1])
        dp[i][1] = max(dp[i - 1][0] - A[i - 1], dp[i - 1][1] + A[i - 1])

    print(dp[n][0])


if __name__ == '__main__':
    resolve2()
