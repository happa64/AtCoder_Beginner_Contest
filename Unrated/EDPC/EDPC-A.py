import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(map(int, input().split()))

    dp = [f_inf for _ in range(n)]
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, n):
        dp[i] = min(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

    print(dp[-1])


if __name__ == '__main__':
    resolve()
